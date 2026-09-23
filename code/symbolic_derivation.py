"""Symbolic identities for the two-type comparison and uniform section."""
import sympy as sp


def two_type_identity():
    B, P, C, S = sp.symbols("B P C S", positive=True)
    ah, al, sh, sl = sp.symbols("alpha_H alpha_L sigma_H sigma_L", positive=True)
    rH = (P - B * sh) / (P * (1 - sh))
    rL = (P - B * sl) / (P * (1 - sl))
    g = lambda sig, r: P - C - (1 - sig) * (r * P - S)
    profit_H = ah * g(sh, rH)
    profit_both = ah * g(sh, rL) + al * g(sl, rL)
    qL = sl * (B - S) - C + S
    corrected = al * qL - ah * (sh - sl) * (B - P) / (1 - sl)
    printed = al * qL - ah * (sh - sl) * (B - P)
    assert sp.factor(profit_both - profit_H - corrected) == 0
    assert sp.factor(printed - corrected) != 0
    order = sp.factor(rL - rH)
    assert sp.factor(order - ((B - P) * (sh - sl) / (P * (1 - sh) * (1 - sl)))) == 0
    return sp.factor(profit_both - profit_H), sp.factor(printed - corrected)


def uniform_identities():
    B, P, C, S, R, SIG = sp.symbols("B P C S R SIG", positive=True)
    h = P * (1 - R) / (B - R * P)
    g = P - C - (1 - SIG) * (R * P - S)
    profit = sp.integrate(g, (SIG, h, 1))
    gh = sp.factor(g.subs(SIG, h))
    derivative_expected = P * (B - P) / (B - R * P) ** 2 * (gh - (B - P) / 2)
    assert sp.factor(sp.diff(profit, R) - derivative_expected) == 0

    r_int = sp.factor((B * (3 * P - 2 * (C - S)) - 2 * P * S - B**2) /
                      (P * (B - 2 * C + P)))
    assert sp.factor(sp.solve(sp.Eq(gh, (B - P) / 2), R)[0] - r_int) == 0
    p_tilde = sp.factor(B * (B + 2 * C - 2 * S) / (3 * B - 2 * S))
    numerator = B * (3 * P - 2 * (C - S)) - 2 * P * S - B**2
    assert sp.factor(numerator - (3 * B - 2 * S) * (P - p_tilde)) == 0

    h_profit = sp.factor(h.subs(R, r_int))
    h_star = (C - S) / (B - S)
    r_star = sp.factor(1 - (C - S) * (B - P) / (P * (B - C)))
    assert sp.factor(h_profit - (B - P + 2 * (C - S)) / (2 * (B - S))) == 0
    assert sp.factor(h.subs(R, r_star) - h_star) == 0

    # Comparative-static signs on the interior branch: x=B-P>0,
    # y=P-C>0, z=C-S>=0, P>0.
    X, Y, Z = sp.symbols("X Y Z", positive=True)
    subs = {B: P + X, C: P - Y, S: P - Y - Z}
    dP = sp.factor(sp.diff(r_int, P).subs(subs))
    dS = sp.factor(sp.diff(r_int, S).subs(subs))
    dC = sp.factor(sp.diff(r_int, C).subs(subs))
    assert sp.factor(dS - 2 * X / (P * (X + 2 * Y))) == 0
    assert sp.factor(dC + 4 * X * (X + Y + Z) / (P * (X + 2 * Y) ** 2)) == 0
    assert sp.factor(dP - (
        3 * P * X**2 + 4 * P * X * Y + 4 * P * X * Z + 4 * P * Y * Z
        + X**3 + 2 * X**2 * Y + 2 * X**2 * Z + 4 * X * Y * Z
    ) / (P**2 * (X + 2 * Y) ** 2)) == 0

    N = sp.symbols("N", positive=True)
    loss_high = N * (B - P) ** 2 / (8 * (B - S))
    assert sp.diff(loss_high, C) == 0
    assert sp.factor(sp.diff(loss_high, P) + N * (B - P) / (4 * (B - S))) == 0
    assert sp.factor(sp.diff(loss_high, S) - N * (B - P) ** 2 /
                      (8 * (B - S) ** 2)) == 0
    return {"profit_derivative": sp.factor(derivative_expected), "refund_root": r_int,
            "price_threshold": p_tilde, "social_refund": r_star,
            "comparative_statics": (dP, dS, dC)}


if __name__ == "__main__":
    print("two-type exact identities:", two_type_identity())
    print("uniform exact identities:", uniform_identities())
    print("PASS: SymPy symbolic derivation")
