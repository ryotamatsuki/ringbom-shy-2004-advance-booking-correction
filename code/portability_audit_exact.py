"""Exact rate-versus-cash normalization and mass-scale audit.

This checker starts from primitive thresholds and payoffs; it does not import
the symbolic derivation or the correspondence implementation.
"""

from fractions import Fraction as Q


def threshold_rate(beta, p, sigma):
    return (p - beta * sigma) / (p * (1 - sigma))


def threshold_cash(beta, p, sigma):
    return (p - beta * sigma) / (1 - sigma)


def unit_profit_rate(p, c, s, sigma, r):
    return p - c - (1 - sigma) * (r * p - s)


def unit_profit_cash(p, c, s, sigma, x):
    return p - c - (1 - sigma) * (x - s)


def rate_gap(beta, p, c, s, alpha_h, alpha_l, sigma_h, sigma_l):
    rh = threshold_rate(beta, p, sigma_h)
    rl = threshold_rate(beta, p, sigma_l)
    return (alpha_l * unit_profit_rate(p, c, s, sigma_l, rl)
            + alpha_h * unit_profit_rate(p, c, s, sigma_h, rl)
            - alpha_h * unit_profit_rate(p, c, s, sigma_h, rh))


def cash_gap(beta, p, c, s, alpha_h, alpha_l, sigma_h, sigma_l):
    xh = threshold_cash(beta, p, sigma_h)
    xl = threshold_cash(beta, p, sigma_l)
    return (alpha_l * unit_profit_cash(p, c, s, sigma_l, xl)
            + alpha_h * unit_profit_cash(p, c, s, sigma_h, xl)
            - alpha_h * unit_profit_cash(p, c, s, sigma_h, xh))


def corrected_closed_form(beta, p, c, s, alpha_h, alpha_l, sigma_h, sigma_l):
    q_l = sigma_l * (beta - s) + s - c
    return (alpha_l * q_l
            - alpha_h * (sigma_h - sigma_l) * (beta - p) / (1 - sigma_l))


def main():
    # The publication's exact regression, plus masses deliberately not summing to one.
    cases = [
        (Q(1), Q(3, 5), Q(1, 50), Q(0), Q(4, 5), Q(1, 5), Q(11, 20), Q(7, 20)),
        (Q(7, 4), Q(1), Q(2, 9), Q(1, 12), Q(3), Q(5, 2), Q(1, 2), Q(1, 5)),
    ]
    for beta, p, c, s, ah, al, sh, sl in cases:
        assert p > 0 and beta > p and sh > sl and sl >= 0 and sh < 1
        rh, rl = threshold_rate(beta, p, sh), threshold_rate(beta, p, sl)
        xh, xl = threshold_cash(beta, p, sh), threshold_cash(beta, p, sl)
        assert Q(0) < rh < rl < Q(1)
        assert xh == p * rh and xl == p * rl
        assert rate_gap(beta, p, c, s, ah, al, sh, sl) == cash_gap(
            beta, p, c, s, ah, al, sh, sl
        )
        assert rate_gap(beta, p, c, s, ah, al, sh, sl) == corrected_closed_form(
            beta, p, c, s, ah, al, sh, sl
        )

    # Tie convention is substantive at boundary points. At beta=p and r=1,
    # weak acceptance serves indifferent consumers; strict rejection gives 0.
    beta = p = Q(1)
    c = s = Q(0)
    sigmas = (Q(3, 5), Q(1, 5))
    masses = (Q(2), Q(3))  # arbitrary positive type masses, not probabilities
    weak_endpoint = sum(
        a * unit_profit_rate(p, c, s, sig, Q(1))
        for a, sig in zip(masses, sigmas)
    )
    strict_endpoint = Q(0)
    assert weak_endpoint == Q(9, 5) and strict_endpoint == 0

    print("PASS: cash-refund normalization preserves the exact corrected gap")
    print("PASS: arbitrary positive type masses preserve the omitted-factor term")
    print("SCOPE: equality branches use source-consistent weak participation")


if __name__ == "__main__":
    main()
