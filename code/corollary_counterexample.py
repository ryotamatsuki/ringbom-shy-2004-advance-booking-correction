"""Exact rational audit of the unqualified high-price Corollary 1 claim.

This checker evaluates the source's primitive expected utility and conditional
seller payoff. It is separate from the symbolic algebra program.
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


if __name__ == "__main__":
    for name, value in audit_point().items():
        print(f"{name}={value}")
