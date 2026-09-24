# v3 vs v2: what changed and why

`paper/Li_draft_v3.tex` (compiled: `Li_draft_v3.pdf`, 35 pp.). v2 is untouched.
Report items refer to `review/Report_quan_JMP_20260923.pdf`.

## Framing and language
- **Title:** *Predictable Play Without a Common Prior*. The abstract and
  introduction were rewritten to state exactly what is assumed (a fixed conjecture;
  common knowledge of `T`, `A` and `u`) and what is dropped (the common prior).
  (report 3.1, D)
- **Introduction** is about 2.5 pages, with one running example (Example 1 plus its
  cap). Wilson framing removed. "Derived from an axiom" removed: Axiom 1 and
  Prop 1 are gone, and the uniform level-0 is justified by the level-k evidence
  as a default. (D, 4.3)
- **Terminology cut:**
  - simple / sensitive / robustly / p-contingent → *predictable (at p / at every
    benchmark)*, *unpredictable*;
  - "floor" → *worst-case margin*;
  - dropped: ripples, ghosts, phantoms, waverers, reduced game, coverage (as a
    term), reference best-response set (as a term), scenario prediction, the
    three-kinds-of-structural-tie anatomy, "Origin does not fix reach", and
    "admissible".
- **Every term is defined before first use, in model order:** conjecture profile →
  uniform conjecture / anchor → benchmark → centred belief → window → prediction
  set / predictability → difference vector → structural / belief-driven → margin →
  dead zone.

## New or changed results
- **Conjecture profile `γ`** is a primitive; the level-1 profile `β` is the leading
  case. All of Section 3 holds for any `γ`, and profiles may differ across players.
- **Lemma 1 (windows)** now gives the exact description: centred ⇔ a mixture of
  window beliefs with positive weight on `q^T = p`. Khintchine is credited. (4.4, C)
- **Lemma 2 (new):** the union over benchmarks of the centred classes is all
  full-support beliefs, so the every-benchmark results do not use centredness. The
  text sorts the results into two groups, those that hold at every benchmark and
  those that hold at a given benchmark. (A, 3.2)
- **Theorem 2 (new):** `b ∈ F_p(t)` if and only if no mixed strategy does at least
  as well at every window belief and strictly better at `p`. The proof is by LP
  duality, for general `γ`. Checked in `review/checks/check_dual.py`.
- **Proposition 4 (new, item B):** perturbed conjectures
  `γ^ε = (1−ε)γ + εR_A`. A structural tie survives if and only if `Σ_a d(a) = 0`.
  The text notes that the ε needed for belief-driven ties depends on `p` (the
  Example 1 numbers checked earlier).
- **Corollary 11 (new):** in the second-price auction with `T ⊆ A`, under `γ^ε`,
  `F_p(t) = {t}` for all types and benchmarks. The "alignment is the unique
  repair" framing is removed. Alignment is now stated as a result about the pure
  level-1 conjecture (merged into Corollary "Bids between values"). (B, 3.3)
- **Section 4.2 (new):** comparison with rationalizability. The sets are
  {0,1},{1,2},{1,2} vs {0},{1,2},{2}. The attribution is corrected: type 1's
  sharpening does not use centredness; type 5's does. (C, 6)
- **The ex-post corollary** is no longer presented as a "fixed point without a
  common prior". (5)

## Corrections
- **Footnote 6** (now in §6): anchors `(1,1,{1,3})` → `(1,{1,3},3)`; the
  mechanism runs through the uniform conjecture. P still falls 1 → 2/3. (4.2)
- **Remark 2 (Recovery)** dropped as vacuous. (4.3)
- **Projection:** only the belief form qualifies, not the equilibrium. (4.3, 5)
- **"Any centred-belief model selects a point inside our sets"** dropped. (5)
- **Tick-size pilot** sentence dropped, since no verified citation was available.
  The Zhang (2026) entry is still marked forthcoming.
- **The roadmap** now covers all sections. The wrong corollary citation in the
  literature section is gone.

## Moved or trimmed
- **Tie anatomy** reduced to Appendix B: pure resolutions are simply conjecture
  profiles; averaging lemma; two-action containment; hedge example; the `w ≠ 1/2`
  fragility of Example 4.
- **Shape-of-classification corollary and reduction lemma** folded into one
  sentence each or dropped.
- **Coarseness evidence** moved into one literature paragraph.

## New sections
- **Concluding remarks:** menu dependence stated candidly (3.5); further rounds of
  reasoning; **n players** (what the proofs need; independence breaks linearity;
  anchors depend on n; tie counting); **testable implications** (item F).

## Not done (per the plan)
- **Item E** (computational predictability–revenue section) and **item G**
  (three-bid dead zones).
- **Bibliography:** the new entries in `ref.bib` (marked "VERIFY") need their
  details checked before submission.
- **Frozen numbers:** unchanged. The regression suite still passes.
