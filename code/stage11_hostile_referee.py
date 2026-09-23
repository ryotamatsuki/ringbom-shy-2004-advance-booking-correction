"""Stage-11 hostile-referee checker written independently from Stage 4/4A code.

It reconstructs reservation utility and seller cash flows from primitives, then
tries to falsify the frozen candidate-set/global-argmax theorem on seeded exact
rational draws spanning beta<p, beta=p, beta>p, zero masses, sigma=0, boundary
thresholds, and arbitrary nonnegative c,s. It imports no project derivation.
"""
from fractions import Fraction as Q
import random

SEED = 112358
DRAWS = 5000
GRID_DEN = 200

def utility(beta, p, sigma, r):
    return sigma * (beta - p) - (1 - sigma) * (1 - r) * p

def profit(beta, p, c, s, a_h, a_l, sh, sl, r):
    out = Q(0)
    for alpha, sigma in ((a_h, sh), (a_l, sl)):
        if alpha > 0 and utility(beta, p, sigma, r) >= 0:
            out += alpha * (
                sigma * (p - c)
                + (1 - sigma) * ((1 - r) * p + s - c)
            )
    return out

def threshold(beta, p, sigma):
    return (p - beta * sigma) / (p * (1 - sigma))

def frozen_candidate_value(beta, p, c, s, a_h, a_l, sh, sl):
    raw = []
    candidates = {Q(0)}
    for alpha, sigma in ((a_h, sh), (a_l, sl)):
        if alpha > 0:
            t = threshold(beta, p, sigma)
            raw.append(t)
            if 0 <= t <= 1:
                candidates.add(t)
    values = {
        r: profit(beta, p, c, s, a_h, a_l, sh, sl, r)
        for r in candidates
    }
    best = max(values.values())
    stars = {r for r, value in values.items() if value == best}
    plateau = None
    if raw and all(t > 0 for t in raw) and best == 0:
        plateau = (Q(0), min(raw))
    return best, stars, plateau

def exact_headline_regression():
    beta, p, c, s = Q(1), Q(3, 5), Q(1, 50), Q(0)
    a_h, a_l = Q(4, 5), Q(1, 5)
    sh, sl = Q(11, 20), Q(7, 20)
    rh, rl = threshold(beta, p, sh), threshold(beta, p, sl)
    assert (rh, rl) == (Q(5, 27), Q(25, 39))
    ph = a_h * profit(beta, p, c, s, Q(1), Q(0), sh, sl, rh)
    # Direct full-population evaluation at each candidate:
    ph = profit(beta, p, c, s, a_h, a_l, sh, sl, rh)
    phl = profit(beta, p, c, s, a_h, a_l, sh, sl, rl)
    assert ph == Q(53, 125)
    assert phl == Q(509, 1300)
    assert phl - ph == -Q(211, 6500)
    printed_margin = (
        a_l * (sl * (beta - s) - c + s)
        - a_h * (sh - sl) * (beta - p)
    )
    corrected_margin = (
        a_l * (sl * (beta - s) - c + s)
        - a_h * (sh - sl) * (beta - p) / (1 - sl)
    )
    assert printed_margin == Q(1, 500)
    assert corrected_margin == -Q(211, 6500)

def directed_boundaries():
    cases = [
        # beta<p, positive-show types: flat no-booking.
        (Q(1,2),Q(4,5),Q(1,5),Q(0),Q(4,5),Q(1,5),Q(3,5),Q(1,5)),
        # beta=p endpoint tie.
        (Q(1),Q(1),Q(0),Q(0),Q(1,2),Q(1,2),Q(3,4),Q(1,4)),
        # sigma_L=0; r_L=1.
        (Q(1),Q(4,5),Q(1,10),Q(1,5),Q(0),Q(1),Q(1,2),Q(0)),
        # r_H=0.
        (Q(1),Q(3,5),Q(1,10),Q(0),Q(1,2),Q(1,2),Q(3,5),Q(1,5)),
        # r_L=0.
        (Q(1),Q(1,5),Q(0),Q(0),Q(1,2),Q(1,2),Q(4,5),Q(1,5)),
        # no-booking dominates feasible endpoints.
        (Q(1),Q(999,1000),Q(9,10),Q(0),Q(1,2),Q(1,2),Q(1,2),Q(1,10)),
        # equal endpoint-profit surface.
        (Q(1),Q(3,5),Q(59,260),Q(0),Q(1,2),Q(1,2),Q(11,20),Q(7,20)),
    ]
    for case in cases:
        best, _, _ = frozen_candidate_value(*case)
        grid_best = max(
            profit(*case, Q(k, GRID_DEN))
            for k in range(GRID_DEN + 1)
        )
        assert best >= grid_best

def random_falsification():
    rng = random.Random(SEED)
    tested = 0
    while tested < DRAWS:
        beta = Q(rng.randint(1, 20), rng.randint(1, 10))
        p = Q(rng.randint(1, 20), rng.randint(1, 10))
        c = Q(rng.randint(0, 20), rng.randint(1, 10))
        s = Q(rng.randint(0, 20), rng.randint(1, 10))
        sigmas = sorted({
            Q(rng.randint(0, 9), 10),
            Q(rng.randint(0, 9), 10),
        })
        if len(sigmas) != 2:
            continue
        sl, sh = sigmas
        if not (0 <= sl < sh < 1):
            continue
        a_h = Q(rng.randint(0, 10), 10)
        a_l = 1 - a_h

        best, stars, plateau = frozen_candidate_value(
            beta, p, c, s, a_h, a_l, sh, sl
        )
        grid_best = max(
            profit(beta, p, c, s, a_h, a_l, sh, sl, Q(k, GRID_DEN))
            for k in range(GRID_DEN + 1)
        )
        assert best >= grid_best
        assert all(0 <= r <= 1 for r in stars)
        if plateau is not None:
            assert best == 0
        tested += 1
    return tested

if __name__ == "__main__":
    exact_headline_regression()
    directed_boundaries()
    tested = random_falsification()
    print({
        "seed": SEED,
        "exact_random_draws": tested,
        "grid_denominator": GRID_DEN,
        "status": "PASS",
    })
