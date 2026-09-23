import Mathlib

namespace RingbomShy

def threshold (β p σ : ℚ) : ℚ := (p - β * σ) / (p * (1 - σ))

def unitProfit (p c s σ r : ℚ) : ℚ := p - c - (1 - σ) * (r * p - s)

def highOnlyProfit (β p c s αH σH : ℚ) : ℚ :=
  αH * unitProfit p c s σH (threshold β p σH)

def bothTypesProfit (β p c s αH αL σH σL : ℚ) : ℚ :=
  αH * unitProfit p c s σH (threshold β p σL) +
    αL * unitProfit p c s σL (threshold β p σL)

def correctedGap (β p c s αH αL σH σL : ℚ) : ℚ :=
  αL * (σL * (β - s) - c + s) -
    αH * (σH - σL) * (β - p) / (1 - σL)

def printedGap (β p c s αH αL σH σL : ℚ) : ℚ :=
  αL * (σL * (β - s) - c + s) -
    αH * (σH - σL) * (β - p)

theorem endpoint_gap_identity
    (β p c s αH αL σH σL : ℚ)
    (hp : p ≠ 0) (hH : σH ≠ 1) (hL : σL ≠ 1) :
    bothTypesProfit β p c s αH αL σH σL -
        highOnlyProfit β p c s αH σH =
      correctedGap β p c s αH αL σH σL := by
  have hOneH : 1 - σH ≠ 0 := by
    intro h
    apply hH
    linarith
  have hOneL : 1 - σL ≠ 0 := by
    intro h
    apply hL
    linarith
  have hDenH : p * (1 - σH) ≠ 0 := mul_ne_zero hp hOneH
  have hDenL : p * (1 - σL) ≠ 0 := mul_ne_zero hp hOneL
  unfold bothTypesProfit highOnlyProfit correctedGap threshold unitProfit
  field_simp [hp, hOneH, hOneL, hDenH, hDenL]
  <;> ring

theorem endpoint_weak_choice_iff
    (β p c s αH αL σH σL : ℚ)
    (hp : p ≠ 0) (hH : σH ≠ 1) (hL : σL ≠ 1) :
    highOnlyProfit β p c s αH σH ≤ bothTypesProfit β p c s αH αL σH σL ↔
      0 ≤ correctedGap β p c s αH αL σH σL := by
  have h := endpoint_gap_identity β p c s αH αL σH σL hp hH hL
  constructor <;> intro hineq <;> nlinarith [h]

theorem endpoint_equality_iff
    (β p c s αH αL σH σL : ℚ)
    (hp : p ≠ 0) (hH : σH ≠ 1) (hL : σL ≠ 1) :
    bothTypesProfit β p c s αH αL σH σL =
        highOnlyProfit β p c s αH σH ↔
      correctedGap β p c s αH αL σH σL = 0 := by
  have h := endpoint_gap_identity β p c s αH αL σH σL hp hH hL
  constructor <;> intro heq <;> nlinarith [h]

theorem printed_gap_factor_omission
    (β p c s αH αL σH σL : ℚ)
    (hL : σL ≠ 1) :
    printedGap β p c s αH αL σH σL -
        correctedGap β p c s αH αL σH σL =
      αH * (σH - σL) * (β - p) * σL / (1 - σL) := by
  have hOneL : 1 - σL ≠ 0 := by
    intro h
    apply hL
    linarith
  unfold printedGap correctedGap
  field_simp [hOneL]
  <;> ring

theorem feasible_endpoint_weak_choice_iff
    (β p c s αH αL σH σL : ℚ)
    (hp : 0 < p) (hH : σH < 1) (hL : σL < 1)
    (hfeasible : 0 ≤ threshold β p σH ∧
      threshold β p σH < threshold β p σL ∧
      threshold β p σL ≤ 1) :
    highOnlyProfit β p c s αH σH ≤
        bothTypesProfit β p c s αH αL σH σL ↔
      0 ≤ correctedGap β p c s αH αL σH σL := by
  exact endpoint_weak_choice_iff β p c s αH αL σH σL
    (ne_of_gt hp) (ne_of_lt hH) (ne_of_lt hL)

theorem corrected_gap_exact_regression :
    threshold 1 (3 / 5) (11 / 20) = 5 / 27 ∧
    threshold 1 (3 / 5) (7 / 20) = 25 / 39 ∧
    highOnlyProfit 1 (3 / 5) (1 / 50) 0 (4 / 5) (11 / 20) = 53 / 125 ∧
    bothTypesProfit 1 (3 / 5) (1 / 50) 0 (4 / 5) (1 / 5) (11 / 20) (7 / 20) =
      509 / 1300 ∧
    bothTypesProfit 1 (3 / 5) (1 / 50) 0 (4 / 5) (1 / 5) (11 / 20) (7 / 20) -
        highOnlyProfit 1 (3 / 5) (1 / 50) 0 (4 / 5) (11 / 20) = -(211 / 6500) ∧
    printedGap 1 (3 / 5) (1 / 50) 0 (4 / 5) (1 / 5) (11 / 20) (7 / 20) = 1 / 500 := by
  norm_num [threshold, highOnlyProfit, bothTypesProfit, unitProfit, printedGap]

theorem exact_regression_feasible :
    0 < threshold 1 (3 / 5) (11 / 20) ∧
    threshold 1 (3 / 5) (11 / 20) < threshold 1 (3 / 5) (7 / 20) ∧
    threshold 1 (3 / 5) (7 / 20) < 1 := by
  norm_num [threshold]

theorem weighted_unit_profit_nonincreasing
    (p c s α σ r₁ r₂ : ℚ)
    (hp : 0 ≤ p) (hα : 0 ≤ α) (hσ : σ ≤ 1) (hr : r₁ ≤ r₂) :
    α * unitProfit p c s σ r₂ ≤ α * unitProfit p c s σ r₁ := by
  have hdiff : unitProfit p c s σ r₂ - unitProfit p c s σ r₁ =
      -(1 - σ) * p * (r₂ - r₁) := by
    unfold unitProfit
    ring
  have hprod : 0 ≤ (1 - σ) * p * (r₂ - r₁) :=
    mul_nonneg (mul_nonneg (by linarith) hp) (by linarith)
  have hunit : unitProfit p c s σ r₂ ≤ unitProfit p c s σ r₁ := by
    nlinarith [hdiff, hprod]
  exact mul_le_mul_of_nonneg_left hunit hα

def fixedSetProfit
    (p c s αH αL σH σL : ℚ) (takeH takeL : Bool) (r : ℚ) : ℚ :=
  (if takeH then αH * unitProfit p c s σH r else 0) +
    (if takeL then αL * unitProfit p c s σL r else 0)

theorem fixed_set_profit_nonincreasing
    (p c s αH αL σH σL r₁ r₂ : ℚ)
    (takeH takeL : Bool)
    (hp : 0 ≤ p) (hαH : 0 ≤ αH) (hαL : 0 ≤ αL)
    (hσH : σH ≤ 1) (hσL : σL ≤ 1) (hr : r₁ ≤ r₂) :
    fixedSetProfit p c s αH αL σH σL takeH takeL r₂ ≤
      fixedSetProfit p c s αH αL σH σL takeH takeL r₁ := by
  have hH := weighted_unit_profit_nonincreasing p c s αH σH r₁ r₂ hp hαH hσH hr
  have hL := weighted_unit_profit_nonincreasing p c s αL σL r₁ r₂ hp hαL hσL hr
  cases takeH <;> cases takeL <;> simp [fixedSetProfit] <;> linarith

def uniformCutoff (β p r : ℚ) : ℚ := p * (1 - r) / (β - r * p)

def uniformProfit (β p c s r : ℚ) : ℚ :=
  let h := uniformCutoff β p r
  let z := r * p - s
  (p - c - z) * (1 - h) + z * (1 - h * h) / 2

def uniformDerivativeBracket (β p c s r : ℚ) : ℚ :=
  s - c + uniformCutoff β p r * (β - s) - (β - p) / 2

def uniformPrivateRoot (β p c s : ℚ) : ℚ :=
  let a := (β - p) / 2 + c - s
  (p * (β - s) - a * β) / (p * ((β - s) - a))

theorem uniform_table1_cost_salvage_tenth_exact :
    uniformPrivateRoot 1 (1 / 2) (1 / 10) (1 / 10) = 8 / 13 ∧
    uniformDerivativeBracket 1 (1 / 2) (1 / 10) (1 / 10) (1 / 4) = 19 / 140 ∧
    uniformProfit 1 (1 / 2) (1 / 10) (1 / 10) (8 / 13) -
      uniformProfit 1 (1 / 2) (1 / 10) (1 / 10) (1 / 4) = 361 / 35280 := by
  norm_num [uniformPrivateRoot, uniformDerivativeBracket, uniformCutoff, uniformProfit]

theorem uniform_table1_zero_cost_salvage_exact :
    uniformPrivateRoot 1 (1 / 2) 0 0 = 2 / 3 ∧
    uniformDerivativeBracket 1 (1 / 2) 0 0 (357 / 1000) = 929 / 6572 ∧
    uniformProfit 1 (1 / 2) 0 0 (2 / 3) -
      uniformProfit 1 (1 / 2) 0 0 (357 / 1000) = 863041 / 86382368 := by
  norm_num [uniformPrivateRoot, uniformDerivativeBracket, uniformCutoff, uniformProfit]

end RingbomShy
