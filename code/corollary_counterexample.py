"""Exact rational audit of the unqualified high-price Corollary 1 claim.

This checker evaluates the source's primitive expected utility and conditional
seller payoff. It is separate from the symbolic algebra program. The manuscript
now gives an analytic near-beta family; the exact points below are regression
checks rather than a substitute for that proof.
"""

from fractions import Fraction as F


def eu(beta, p, sigma, r):
    return sigma * (beta - p) - (1 - sigma) * (1 - r) * p


def conditional_profit(p, c, s, sigma, r):
    show = sigma * (p - c)
    no_show = (1 - sigma) * ((1 - r) * p + s - c)
    return show + no_show


def expected_profit(beta, p, c, s, a_h, a_l, sig_h, sig_l, r):
    total = F(0)
    for mass, sigma in ((a_h, sig_h), (a_l, sig_l)):
        if eu(beta, p, sigma, r) >= 0:
            total += mass * conditional_profit(p, c, s, sigma, r)
    return total


def audit_point():
    beta = F(1)
    p = F(999, 1000)
    c = F(9, 10)
    s = F(0)
    a_h = a_l = F(1, 2)
    sig_h = F(1, 2)
    sig_l = F(1, 10)
    r_h = (p - beta * sig_h) / (p * (1 - sig_h))
    r_l = (p - beta * sig_l) / (p * (1 - sig_l))
    pi_none = F(0)
    pi_h = expected_profit(beta, p, c, s, a_h, a_l, sig_h, sig_l, r_h)
    pi_both = expected_profit(beta, p, c, s, a_h, a_l, sig_h, sig_l, r_l)
    q_l = sig_l * (beta - s) + s - c
    corrected_delta = a_l * q_l - a_h * (sig_h - sig_l) * (beta - p) / (1 - sig_l)
    printed_delta = a_l * q_l - a_h * (sig_h - sig_l) * (beta - p)
    assert 0 < r_h < r_l < 1
    assert pi_none == 0 > pi_h
    assert pi_none == 0 > pi_both
    assert corrected_delta == pi_both - pi_h < 0
    return {
        "beta": beta,
        "p": p,
        "r_h": r_h,
        "r_l": r_l,
        "profit_none": pi_none,
        "profit_h_at_r_h": pi_h,
        "profit_both_at_r_l": pi_both,
        "corrected_endpoint_difference": corrected_delta,
        "printed_condition_lhs_minus_rhs": printed_delta,
    }


def audit_high_price_family_regressions():
    """Directed exact points approaching beta for the fixed counterexample family."""
    beta = F(1)
    c = F(9, 10)
    s = F(0)
    a_h = a_l = F(1, 2)
    sig_h = F(1, 2)
    sig_l = F(1, 10)
    q_h = sig_h * (beta - s) + s - c
    q_l = sig_l * (beta - s) + s - c
    assert (q_h, q_l) == (F(-2, 5), F(-4, 5))

    rows = []
    for p in (F(3, 4), F(9, 10), F(99, 100), F(999, 1000)):
        r_h = (p - beta * sig_h) / (p * (1 - sig_h))
        r_l = (p - beta * sig_l) / (p * (1 - sig_l))
        pi_h = expected_profit(beta, p, c, s, a_h, a_l, sig_h, sig_l, r_h)
        pi_both = expected_profit(beta, p, c, s, a_h, a_l, sig_h, sig_l, r_l)
        assert 0 < r_h < r_l < 1
        assert pi_h == F(-1, 5)
        assert pi_both < pi_h < 0
        assert expected_profit(beta, p, c, s, a_h, a_l, sig_h, sig_l, F(0)) == 0
        rows.append((p, r_h, r_l, pi_h, pi_both))
    return rows


if __name__ == "__main__":
    for name, value in audit_point().items():
        print(f"{name}={value}")
    for row in audit_high_price_family_regressions():
        print("near_beta_regression=", row)
    print("PASS: high-price Corollary 1 qualification remains necessary arbitrarily near beta")
