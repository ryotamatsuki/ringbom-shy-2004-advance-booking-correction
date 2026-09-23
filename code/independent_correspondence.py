"""Independent exact-rational enumerator for the two-type global argmax.

Unlike the symbolic derivation, this program never substitutes a threshold into
an algebraic profit formula. It tests raw expected utility at each candidate
and sums state-contingent seller cash flows directly.
"""
from fractions import Fraction as Q
import random


def utility(beta, p, sigma, r):
    return sigma * (beta - p) - (1 - sigma) * (1 - r) * p


def raw_profit_at(beta, p, c, s, a_h, a_l, sh, sl, r):
    profit = Q(0)
    for alpha, sigma in ((a_h, sh), (a_l, sl)):
        if utility(beta, p, sigma, r) >= 0:
            profit += alpha * (
                sigma * (p - c)
                + (1 - sigma) * ((1 - r) * p + s - c)
            )
    return profit


def raw_threshold(beta, p, sigma):
    return (p - beta * sigma) / (p * (1 - sigma))


def correspondence(beta, p, c, s, a_h, a_l, sh, sl):
    """Return exact maximum value, isolated maximizers, and any flat set.

    Assumes p>0, beta>0, 0<=a_i, a_H+a_L=1, 0<=sigma_L<=sigma_H<1.
    Participation at equality is weak. For beta<p, only sigma=0 types can
    participate, and only at r=1; for beta=p, r=1 makes both types indifferent.
    """
    assert p > 0 and beta > 0
    assert a_h >= 0 and a_l >= 0 and a_h + a_l == 1
    assert 0 <= sl <= sh < 1

    if beta < p:
        endpoint = raw_profit_at(beta, p, c, s, a_h, a_l, sh, sl, Q(1))
        if endpoint > 0:
            return endpoint, (Q(1),), None
        if endpoint == 0:
            return Q(0), (), (Q(0), Q(1), "closed")
        return Q(0), (), (Q(0), Q(1), "right-open")

    if beta == p:
        endpoint = raw_profit_at(beta, p, c, s, a_h, a_l, sh, sl, Q(1))
        if endpoint > 0:
            return endpoint, (Q(1),), None
        if endpoint == 0:
            return Q(0), (), (Q(0), Q(1), "closed")
        return Q(0), (), (Q(0), Q(1), "right-open")

    thresholds = []
    for alpha, sigma in ((a_h, sh), (a_l, sl)):
        if alpha > 0:
            t = raw_threshold(beta, p, sigma)
            if 0 < t <= 1:
                thresholds.append(t)

    candidates = sorted({Q(0), *thresholds})
    values = {r: raw_profit_at(beta, p, c, s, a_h, a_l, sh, sl, r) for r in candidates}
    best = max(values.values())
    maximizers = tuple(r for r, value in values.items() if value == best)

    # On a fixed nonempty participation region profit strictly decreases in r.
    # Before the first positive-mass threshold, profit is identically zero.
    starts_with_no_bookings = not any(
        alpha > 0 and utility(beta, p, sigma, Q(0)) >= 0
        for alpha, sigma in ((a_h, sh), (a_l, sl))
    )
    positive_thresholds = [t for t in thresholds if t > 0]
    flat = None
    if best == 0 and starts_with_no_bookings and positive_thresholds:
        flat = (Q(0), min(positive_thresholds), "right-open")

    return best, maximizers, flat


def sampled_rationals(seed=20040923, draws=800):
    rng = random.Random(seed)
    for _ in range(draws):
        # Exact rational parameters. Include beta>p cases with both signs of
        # entry margins, and include mass limits alpha_i=0 or 1.
        p = Q(rng.randint(1, 9), rng.randint(1, 5))
        beta = p + Q(rng.randint(1, 7), rng.randint(1, 4))
        sh = Q(rng.randint(2, 9), 10)
        sl = Q(rng.randint(0, max(0, int(sh * 10) - 1)), 10)
        if sh == sl:
            sh = min(Q(9, 10), sh + Q(1, 10))
        a_h = Q(rng.randint(0, 10), 10)
        a_l = 1 - a_h
        c = Q(rng.randint(0, 10), 10) * p
        s = Q(rng.randint(0, 10), 10) * c

        best, maximizers, flat = correspondence(beta, p, c, s, a_h, a_l, sh, sl)
        # Finite exact grid is a falsification cross-check, not the proof of
        # globality. Thresholds are also checked exactly in `maximizers`.
        grid = [Q(k, 400) for k in range(401)]
        grid_best = max(raw_profit_at(beta, p, c, s, a_h, a_l, sh, sl, r) for r in grid)
        assert best >= grid_best
        assert all(0 <= r <= 1 for r in maximizers)
        if flat is not None:
            assert best == 0 and flat[0] == 0 and flat[1] > 0
    return draws


def edge_regressions():
    count = 0

    def run(case):
        nonlocal count
        correspondence(*case)
        count += 1

    # Interior counterexample and endpoint cases with negative/absent masses.
    case = (Q(1), Q(3, 5), Q(1, 50), Q(0), Q(4, 5), Q(1, 5), Q(11, 20), Q(7, 20))
    run(case)
    assert correspondence(*case) == (Q(53, 125), (Q(5, 27),), None)

    negative_h_cutoff = (Q(1), Q(4, 5), Q(1, 5), Q(1, 10), Q(4, 5), Q(1, 5), Q(9, 10), Q(1, 10))
    run(negative_h_cutoff)
    assert correspondence(*negative_h_cutoff) == (Q(61, 125), (Q(0),), None)

    absent_low = (Q(1), Q(3, 5), Q(2, 5), Q(0), Q(1), Q(0), Q(3, 5), Q(1, 5))
    run(absent_low)
    merged_types = (Q(1), Q(3, 5), Q(2, 5), Q(0), Q(1, 2), Q(1, 2), Q(2, 5), Q(2, 5))
    run(merged_types)

    # Both thresholds are below zero: full participation holds already at r=0.
    full = (Q(1), Q(3, 5), Q(1, 10), Q(0), Q(1, 2), Q(1, 2), Q(9, 10), Q(4, 5))
    run(full)
    assert utility(Q(1), Q(3, 5), Q(9, 10), Q(0)) > 0
    assert utility(Q(1), Q(3, 5), Q(4, 5), Q(0)) > 0

    # The exact beta=p boundary: r<1 has no participation, r=1 is a tie.
    beta_p_positive = (Q(1), Q(1), Q(0), Q(0), Q(1, 2), Q(1, 2), Q(3, 4), Q(1, 4))
    run(beta_p_positive)
    assert correspondence(*beta_p_positive)[1] == (Q(1),)
    beta_p_negative = (Q(1), Q(1), Q(2), Q(0), Q(1, 2), Q(1, 2), Q(3, 4), Q(1, 4))
    run(beta_p_negative)
    assert correspondence(*beta_p_negative)[2] == (Q(0), Q(1), "right-open")

    # beta<p with positive-show types: no reservations for every refund.
    beta_below_p = (Q(1, 2), Q(4, 5), Q(1, 5), Q(0), Q(4, 5), Q(1, 5), Q(3, 5), Q(1, 5))
    run(beta_below_p)
    assert correspondence(*beta_below_p)[2] == (Q(0), Q(1), "closed")

    # A source-domain point where nonparticipation defeats both feasible endpoints.
    no_booking = (Q(1), Q(4, 5), Q(7, 10), Q(0), Q(4, 5), Q(1, 5), Q(1, 5), Q(1, 10))
    run(no_booking)
    assert correspondence(*no_booking)[2] == (Q(0), Q(15, 16), "right-open")

    # Exact sigma=0 endpoint tie when beta<p; test each sign of s-c.
    zero_show_cases = [
        (Q(1, 2), Q(4, 5), Q(1, 10), Q(1, 5), Q(4, 5), Q(1, 5), Q(1, 2), Q(0)),
        (Q(1, 2), Q(4, 5), Q(1, 5), Q(1, 5), Q(4, 5), Q(1, 5), Q(1, 2), Q(0)),
        (Q(1, 2), Q(4, 5), Q(3, 10), Q(1, 5), Q(4, 5), Q(1, 5), Q(1, 2), Q(0)),
    ]
    for item in zero_show_cases:
        run(item)
    assert correspondence(*zero_show_cases[0])[1] == (Q(1),)
    assert correspondence(*zero_show_cases[1])[2] == (Q(0), Q(1), "closed")
    assert correspondence(*zero_show_cases[2])[2] == (Q(0), Q(1), "right-open")

    # With beta>p and sigma_L=0, r_L=1; include either mass limit and all profit signs.
    zero_show_r1_cases = [
        (Q(1), Q(4, 5), Q(1, 10), Q(1, 5), Q(0), Q(1), Q(1, 2), Q(0)),
        (Q(1), Q(4, 5), Q(1, 5), Q(1, 5), Q(0), Q(1), Q(1, 2), Q(0)),
        (Q(1), Q(4, 5), Q(3, 10), Q(1, 5), Q(0), Q(1), Q(1, 2), Q(0)),
    ]
    for item in zero_show_r1_cases:
        run(item)
    assert raw_threshold(Q(1), Q(4, 5), Q(0)) == 1
    assert correspondence(*zero_show_r1_cases[0])[1] == (Q(1),)

    # r_H=0: the high type is indifferent at the strategy lower boundary.
    r_h_zero = (Q(1), Q(3, 5), Q(1, 10), Q(0), Q(1, 2), Q(1, 2), Q(3, 5), Q(1, 5))
    run(r_h_zero)
    assert raw_threshold(Q(1), Q(3, 5), Q(3, 5)) == 0
    assert correspondence(*r_h_zero)[2] is None

    # Exact equality surface for the corrected endpoint comparison.
    equal_profit = (Q(1), Q(3, 5), Q(59, 260), Q(0), Q(1, 2), Q(1, 2), Q(11, 20), Q(7, 20))
    run(equal_profit)
    eq_result = correspondence(*equal_profit)
    assert eq_result[0] == Q(21, 130)
    assert eq_result[1] == (Q(5, 27), Q(25, 39))

    # High-price counterexample to the unqualified Corollary 1 claim.
    high_price = (Q(1), Q(999, 1000), Q(9, 10), Q(0), Q(1, 2), Q(1, 2), Q(1, 2), Q(1, 10))
    run(high_price)
    high_result = correspondence(*high_price)
    assert high_result[0] == 0
    assert raw_threshold(Q(1), Q(999, 1000), Q(1, 2)) == Q(998, 999)
    assert raw_threshold(Q(1), Q(999, 1000), Q(1, 10)) == Q(8990, 8991)

    # Limit stresses: sigma_L near zero, sigma_H near one, and p near c=s.
    near_extremes = (Q(1), Q(999, 1000), Q(1, 2), Q(0), Q(1, 2), Q(1, 2), Q(999, 1000), Q(1, 1000))
    run(near_extremes)
    near_cost_boundary = (Q(1), Q(4, 5), Q(799, 1000), Q(799, 1000), Q(1, 2), Q(1, 2), Q(3, 5), Q(1, 5))
    run(near_cost_boundary)

    # r_L=0: low type is exactly indifferent at r=0 while H already participates.
    r_l_zero = (Q(1), Q(1, 5), Q(0), Q(0), Q(1, 2), Q(1, 2), Q(4, 5), Q(1, 5))
    run(r_l_zero)
    assert raw_threshold(Q(1), Q(1, 5), Q(1, 5)) == 0

    return count


if __name__ == "__main__":
    print({"exact_random_rational_draws": sampled_rationals(), "edge_regressions": edge_regressions()})
    print("PASS: independent primitive-payoff correspondence checker")
