"""Exact recheck of Ringbom--Shy (2004) uniform Tables 1 and 2.

This checker starts from the primitive cutoff and per-reservation payoff. It
derives the private stationary refund from the boundary condition in the
uniform profit derivative, integrates primitive profits exactly, and computes
welfare loss from the two cutoffs. It does not import symbolic_derivation.py.
"""

from decimal import Decimal, ROUND_HALF_UP, localcontext
from fractions import Fraction as Q


BETA = Q(1)
PRICES = (Q(4, 5), Q(3, 5), Q(1, 2), Q(2, 5))
COSTS = ((Q(1, 5), Q(1, 10)), (Q(1, 10), Q(1, 10)),
         (Q(1, 10), Q(0)), (Q(0), Q(0)))

# Transcribed from the publisher VOR, Table 1 (private rate, then social rate).
TABLE1_PRIVATE = (
    ("0.929", "0.969", "0.9375", "0.972"),
    ("0.667", "0.810", "0.714", "0.833"),
    ("0.364", "0.250", "0.462", "0.357"),
    ("0.000", "0.250", "0.000", "0.357"),
)
TABLE1_SOCIAL = (
    ("0.969", "1", "0.972", "1"),
    ("0.917", "1", "0.926", "1"),
    ("0.875", "1", "0.889", "1"),
    ("0.8125", "1", "0.833", "1"),
)

# Transcribed from the publisher VOR, Table 2, for n=1000.
TABLE2_LOSS = (
    ("5.556", "5.556", "5.000", "5.000"),
    ("22.22", "22.22", "20.00", "20.00"),
    ("34.72", "34.72", "31.25", "31.25"),
    ("37.56", "50.00", "45.00", "45.00"),
)


def cutoff(beta: Q, price: Q, refund: Q) -> Q:
    return price * (1 - refund) / (beta - refund * price)


def primitive_profit(beta: Q, price: Q, cost: Q, salvage: Q, refund: Q) -> Q:
    """Integrate the primitive seller payoff over reserving uniform types."""
    h = cutoff(beta, price, refund)
    no_show_net = refund * price - salvage
    return (price - cost - no_show_net) * (1 - h) + no_show_net * (1 - h * h) / 2


def derivative_bracket(beta: Q, price: Q, cost: Q, salvage: Q, refund: Q) -> Q:
    """Sign-equivalent bracket in dπ/dr after direct Leibniz differentiation."""
    h = cutoff(beta, price, refund)
    marginal_unit_profit = salvage - cost + h * (beta - salvage)
    return marginal_unit_profit - (beta - price) / 2


def private_root_from_boundary_foc(beta: Q, price: Q, cost: Q, salvage: Q) -> Q:
    """Solve g_{h(r)}=(β-p)/2 using the primitive cutoff and payoff."""
    rhs_adjustment = (beta - price) / 2 + cost - salvage
    numerator = price * (beta - salvage) - rhs_adjustment * beta
    denominator = price * ((beta - salvage) - rhs_adjustment)
    if denominator == 0:
        raise ZeroDivisionError("unexpected degenerate FOC in the table domain")
    return numerator / denominator


def social_refund(beta: Q, price: Q, cost: Q, salvage: Q) -> Q:
    social_cutoff = (cost - salvage) / (beta - salvage)
    return (price - beta * social_cutoff) / (price * (1 - social_cutoff))


def direct_welfare_loss(beta: Q, price: Q, cost: Q, salvage: Q,
                        private_refund: Q, n: Q = Q(1000)) -> Q:
    private_cutoff = cutoff(beta, price, private_refund)
    social_cutoff = (cost - salvage) / (beta - salvage)
    return n * (beta - salvage) * (private_cutoff - social_cutoff) ** 2 / 2


def round_like_source(value: Q, source_string: str) -> str:
    places = len(source_string.partition(".")[2])
    quantum = Decimal(1).scaleb(-places)
    with localcontext() as ctx:
        ctx.prec = 40
        dec = Decimal(value.numerator) / Decimal(value.denominator)
        return format(dec.quantize(quantum, rounding=ROUND_HALF_UP), f".{places}f")


def run() -> dict:
    private_mismatches = []
    social_mismatches = []
    loss_mismatches = []
    results = []

    for row, price in enumerate(PRICES):
        private_row = []
        social_row = []
        loss_row = []
        for col, (cost, salvage) in enumerate(COSTS):
            root = private_root_from_boundary_foc(BETA, price, cost, salvage)
            private = max(Q(0), root)
            social = social_refund(BETA, price, cost, salvage)
            assert 0 <= private <= 1 and 0 <= social <= 1

            # The sign factor p(β-p)/(β-rp)^2 is positive; the bracket is
            # strictly decreasing because the cutoff is strictly decreasing.
            b0 = derivative_bracket(BETA, price, cost, salvage, Q(0))
            if root <= 0:
                assert b0 <= 0
                assert derivative_bracket(BETA, price, cost, salvage, private) <= 0
            else:
                assert derivative_bracket(BETA, price, cost, salvage, private) == 0

            ptext = TABLE1_PRIVATE[row][col]
            stext = TABLE1_SOCIAL[row][col]
            got_private = round_like_source(private, ptext)
            got_social = round_like_source(social, stext)
            if got_private != ptext:
                private_mismatches.append((str(price), str(cost), str(salvage), ptext,
                                           str(private), got_private))
            if got_social != stext:
                social_mismatches.append((str(price), str(cost), str(salvage), stext,
                                          str(social), got_social))

            loss = direct_welfare_loss(BETA, price, cost, salvage, private)
            ltext = TABLE2_LOSS[row][col]
            got_loss = round_like_source(loss, ltext)
            if got_loss != ltext:
                loss_mismatches.append((str(price), str(cost), str(salvage), ltext,
                                        str(loss), got_loss))

            # Direct payoff comparison at the two disputed Table 1 values.
            if row == 2 and col in (1, 3):
                printed = Q(ptext)
                gain = primitive_profit(BETA, price, cost, salvage, private) - \
                    primitive_profit(BETA, price, cost, salvage, printed)
                assert gain > 0
                assert derivative_bracket(BETA, price, cost, salvage, printed) > 0
                private_row.append((ptext, str(private), str(gain)))
            else:
                private_row.append((ptext, str(private), ""))
            social_row.append((stext, str(social)))
            loss_row.append((ltext, str(loss)))

        results.append((str(price), private_row, social_row, loss_row))

    expected_errors = {
        ("1/2", "1/10", "1/10", "0.250"),
        ("1/2", "0", "0", "0.357"),
    }
    observed_errors = {(p, c, s, source) for p, c, s, source, _, _ in private_mismatches}
    assert observed_errors == expected_errors
    assert not social_mismatches
    assert not loss_mismatches

    return {
        "table1_private_mismatches": private_mismatches,
        "table1_social_mismatches": social_mismatches,
        "table2_loss_mismatches": loss_mismatches,
        "exact_reproduction_rows": results,
        "disputed_cells_direct_profit_gain": [
            result for result in results[2][1] if result[2]
        ],
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(run())
    print("PASS: uniform tables exactly checked from primitive payoff/cutoffs")
