"""Exact rational checks for uniform-model boundary behavior.

This script evaluates formulas and primitive utilities directly at limits that
are excluded from the paper's strict active domain.
"""
from fractions import Fraction as F


def utility(beta, p, sigma, r):
    return sigma * (beta - p) - (1 - sigma) * (1 - r) * p


def private_refund(beta, p, c, s):
    r_int = (
        beta * (3 * p - 2 * (c - s)) - 2 * p * s - beta**2
    ) / (p * (beta - 2 * c + p))
    return max(F(0), r_int)


def social_refund(beta, p, c, s):
    return 1 - (c - s) * (beta - p) / (p * (beta - c))


def run():
    beta = F(1)
    p_equal_cost = c = F(4, 5)
    s = F(0)
    r_bar = private_refund(beta, p_equal_cost, c, s)
    r_star = social_refund(beta, p_equal_cost, c, s)
    private_cutoff = p_equal_cost / beta
    social_cutoff = (c - s) / (beta - s)
    assert (r_bar, r_star) == (0, 0)
    assert private_cutoff == social_cutoff == F(4, 5)

    p_above_cost = F(801, 1000)
    r_bar_inside = private_refund(beta, p_above_cost, c, s)
    r_star_inside = social_refund(beta, p_above_cost, c, s)
    assert p_above_cost > c and r_star_inside > r_bar_inside

    # p>c is sufficient for the strict comparison on the audited interior domain,
    # but it is not a pointwise necessary condition after leaving that domain.
    beta2 = F(1)
    p2 = c2 = F(1, 2)
    s2 = F(1, 4)
    r_bar_p_eq_c_salvage = private_refund(beta2, p2, c2, s2)
    r_star_p_eq_c_salvage = social_refund(beta2, p2, c2, s2)
    assert (r_bar_p_eq_c_salvage, r_star_p_eq_c_salvage) == (F(0), F(1, 2))

    # At beta=p, r=1, all types are indifferent; the cutoff formula is 0/0.
    assert all(utility(F(1), F(1), sig, F(1)) == 0 for sig in (F(0), F(1, 2), F(1)))

    # At beta<p and beta-rp=0, direct utility is beta-p<0 for every sigma.
    beta_below_price, price, refund = F(4, 5), F(1), F(4, 5)
    denominator = beta_below_price - refund * price
    assert denominator == 0
    assert all(
        utility(beta_below_price, price, sig, refund) == F(-1, 5)
        for sig in (F(0), F(1, 2), F(1))
    )

    # For p>beta, positive-show types never reserve, even at full refund.
    high_price = F(6, 5)
    assert utility(F(1), high_price, F(1, 2), F(1)) < 0
    assert utility(F(1), high_price, F(1), F(1)) < 0
    return {
        "p_equals_c_s_zero": (r_bar, r_star, private_cutoff, social_cutoff),
        "p_strictly_above_c": (r_bar_inside, r_star_inside),
        "p_equals_c_with_positive_salvage": (r_bar_p_eq_c_salvage, r_star_p_eq_c_salvage),
        "beta_equals_p_full_refund": "all types indifferent",
        "beta_minus_rp_zero": "direct utility is beta-p < 0 for every type",
        "p_above_beta": "no positive-show types participate",
    }


if __name__ == "__main__":
    print(run())
    print("PASS: exact uniform boundary audit")
