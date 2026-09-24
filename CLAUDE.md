# belief-free — "Simple Strategies in Information Ripples" (Li Quan, JMP)

Theory working paper, Faculty of Economics, Cambridge. This repo holds the draft,
the referee report driving the current revision, and verification scripts.

## Files

- `paper/Li_draft_v2.tex`, `paper/ref.bib` — current draft (August 2026). Compile:
  `pdflatex → bibtex → pdflatex ×2` (natbib, apalike, tikz).
- `review/Report_quan_JMP_20260923.pdf` — referee-style report (Claude, prompted by
  supervisor), 23 Sep 2026. Recommendation: major revision; 2-month plan, items A–G.
- `review/checks/check_report.py` (+ `.out`) — exact checks of the report's claims.
- `review/notes_borgers_li.md` — comparison with Börgers–Li (2019) and revision
  proposals from it (incl. a proposed dominance dual for membership in `F_p(t)`).
- `setup.sh` — cloud environment setup (Python science stack, LaTeX).

## Model in one paragraph

Finite `T ⊂ ℝ` (perceived types, coarse), finite `A` (actions/bids), symmetric
private-value payoff `u(b, b'; t)`. Reference `R_A` = uniform on `A` (Axiom 1 /
Prop 1). Anchor `β(s)` = uniform mix over `B⁰(s) = argmax_b Σ_{b'} u(b,b';s)`.
Belief `q` is *centred at t*: `q_s/p_s` single-peaked at `t` relative to analyst
benchmark `p`. `U^t_q(b) = Σ_s q_s ū(b, β(s); t)`. Prediction set
`F_p(t) = ∪_{q∈Q_p(t)} argmax U^t_q`; simple ⇔ singleton; predictability
`P(p)` = p-mass of simple types. Difference vector `δ_s` = advantage of `b` over
`b'` against believed type `s`.

Key results: Lemma 1 (closure of `Q_p(t)` = hull of window restrictions `q^W`);
Theorem 1(i) window test at fixed `p`; Theorem 1(ii) robust simplicity ⇔
reduced-game weak dominance; Prop 2 structural (`δ=0`) vs belief-driven ties;
two-bid FPA caps / dead zone `(a₂, 2a₂−a₁)`; SPA gaps, alignment `A=T`.

Running examples: FPA `T={1,3,5}`, `A={0,1,2}` (P=2/3 uniform); cap `A={0,1}`
(P=1); SPA `A={0..5}` (P=0); tied anchor FPA `A={0,2}`.

## Verification rules (non-negotiable)

- Use the `information-ripples-verify` skill (`ripples.py`, `caps.py`,
  `regression.py`) for any numerical or universal claim. Exact `Fraction`
  arithmetic only — never floats (ties must be exactly zero).
- A search is not a proof: report "no counterexample in N cases" with its scope.
- Simplicity at a fixed `p` can be decided exactly by the Theorem 1(i) window test
  (see `simple_at` in `review/checks/check_report.py`); prefer it to belief sampling.
- Frozen numbers (see skill) change only with the author's approval.

## Status of the referee report (checked 24 Sep 2026)

Confirmed exactly:
- §3.2: `q = p` is always centred, so robust simplicity (and every "P=1 at every
  benchmark" result: caps, dead zone, SPA gaps/alignment/margins) does not use
  centredness. Centredness matters only at a fixed benchmark and for robust
  sensitivity.
- §3.3 / item B(iii): with anchors perturbed toward the reference,
  `β_ε = (1−ε)β + εR_A`, SPA gives `P=1` for every ε>0 on every grid ⊇ T
  (proof: truth weakly dominates in the full game, strictly against the rival
  bid itself). This overturns "alignment is the unique repair" (Cor 9).
- Footnote 6, second witness (`T={2,4,6}`, `A={0,1,3}`): anchors are
  `(1,1,{1,3})`, not `(1,3,3)`; after deleting bid 0 they become `(1,{1,3},3)`.
  P still falls 1 → 2/3.
- §6: in Example 1, rationalizable sets are `{0,1}, {1,2}, {1,2}` vs
  `F_p = {0}, {1,2}, {2}` (uniform).

Additions beyond the report:
- The sharpening for type 1 (`{0}` vs `{0,1}`) comes from anchoring + full
  support, not centredness (type 1 is robustly simple, a class-free result).
  The report attributes it to centredness; only type 5's sharpening is class-dependent.
- Item B(ii) holds pointwise in `p` only: at fixed ε=1/100, Example 1 type 3
  becomes simple (bid 1) at `p=(.4995,.4995,.001)`. Pairs with `Σ_a d(a)=0`
  (e.g. tied example `A={0,2}`) survive exactly. State the ε/p quantifier order.

## Conventions

- Author-facing prose: British spelling (as in the draft).
- Don't invent new theorems into the draft without the author's approval;
  propose text in separate files or chat first.
- Commit and push work every session (container is ephemeral).
