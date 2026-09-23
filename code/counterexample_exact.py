"""Exact rational check using the source's primitive utility and payoff."""
from fractions import Fraction as Q


def eu(beta, price, show, refund):
    return show * (beta - price) - (1 - show) * (1 - refund) * price


def unit_profit(price, cost, salvage, show, refund):
    # State-contingent accounting: show -> p-c; no-show -> (1-r)p+s-c.
    return show * (price - cost) + (1 - show) * ((1 - refund) * price + salvage - cost)


def market_profit(params, refund):
    beta, price, cost, salvage, alpha_h, alpha_l, show_h, show_l = params
    total = Q(0)
    for mass, show in ((alpha_h, show_h), (alpha_l, show_l)):
        if eu(beta, price, show, refund) >= 0:  # weak participation, as in source Eq. (7)
            total += mass * unit_profit(price, cost, salvage, show, refund)
    return total


def run():
    beta, price, cost, salvage = Q(1), Q(3, 5), Q(1, 50), Q(0)
    alpha_h, alpha_l = Q(4, 5), Q(1, 5)
    show_h, show_l = Q(11, 20), Q(7, 20)
    params = (beta, price, cost, salvage, alpha_h, alpha_l, show_h, show_l)
    r_h = (price - beta * show_h) / (price * (1 - show_h))
    r_l = (price - beta * show_l) / (price * (1 - show_l))

    # These profits are recomputed by the primitive decision rule above.
    pi_honly = market_profit(params, r_h)
    pi_both = market_profit(params, r_l)
    direct_difference = pi_both - pi_honly

    # Separately evaluate the inequality printed in the VOR's Eq. (6).
    q_l = show_l * (beta - salvage) - cost + salvage
    printed_lhs_minus_rhs = (
        alpha_l * q_l - alpha_h * (show_h - show_l) * (beta - price)
    )

    assert (r_h, r_l) == (Q(5, 27), Q(25, 39))
    assert 0 < r_h < r_l < 1
    assert pi_honly == Q(53, 125)
    assert pi_both == Q(509, 1300)
    assert direct_difference == Q(-211, 6500)
    assert printed_lhs_minus_rhs == Q(1, 500) > 0
    assert (eu(beta, price, show_h, r_h), eu(beta, price, show_l, r_h)) == (0, Q(-8, 45))
    assert eu(beta, price, show_l, r_l) == 0

    print({
        "r_H": str(r_h),
        "r_L": str(r_l),
        "primitive_profit_H_only": str(pi_honly),
        "primitive_profit_both": str(pi_both),
        "primitive_difference": str(direct_difference),
        "printed_eq6_lhs_minus_rhs": str(printed_lhs_minus_rhs),
        "verdict": "printed rule chooses r_L, primitive profits choose r_H",
    })


if __name__ == "__main__":
    run()
