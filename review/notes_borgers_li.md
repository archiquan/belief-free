# Börgers & Li (2019, Econometrica) vs. this paper: notes for the revision

Read 24 Sep 2026 at the author's request, before any edits to the draft.
Status: proposals only. Nothing below is in the draft yet.

## 1. The two constructions side by side

| | Börgers–Li (BL) | This paper |
|---|---|---|
| Utility belief (about opponent's type) | fixed `μ_i`; an argument of the outcome correspondence | ranges over the centred class `Q_p(t)` |
| Strategic belief (about opponent's action) | every belief compatible with `μ_i`: type `u_j` plays anything in `UD_j(u_j)` (not weakly dominated) | one belief: type `s` plays its anchor `β(s)` |
| Operator | ∩ over strategic beliefs (robustness) | ∪ over utility beliefs (possibility) |
| Own choice | restricted to `UD_i(u_i)` (the agent's own undominated actions) | argmax over all of `A` |
| Indifference | ruled out (strict vNM utilities over outcomes) | allowed; the source of structural ties |
| Headline | characterise *mechanisms* (local dictatorship) under richness | characterise *types* (window test, dominance) |

Formal link: a best response to the full-support uniform reference is never weakly
dominated, so `β(s) ∈ Δ(UD(s))`. The anchored conjecture is therefore **one of
BL's compatible strategic beliefs**. At a fixed `q`, BL's intersection (when
non-empty) is contained in this paper's argmax, so the union of BL's sets over
centred `q` is contained in `F_p(t)`.

## 2. Consequences for the revision

1. **The measure is a robustness object.** `|∪_q argmax| = 1` if and only if the
   same single action is the unique argmax at every `q`, which is an intersection
   statement. So `P(p)` is a robustness measure like BL's. The union ("possibility")
   has content only at sensitive types, and the draft (end of §3) leaves that open.
2. **The SPA structural ties are a failure of own admissibility.** In the SPA with
   `T ⊆ A`, `UD(s) = {s}`, so BL's compatible set is exactly `β`. BL still predict
   truth uniquely, because they restrict the agent's own choice to `UD(t) = {t}`.
   The gap bids are weakly dominated in the full game. So the paper's structural
   sensitivity comes from allowing weakly dominated own choices, which is the same
   diagnosis as the report's item B, reached from BL's side.
3. **A tie-break internal to the model.** The agent already holds `R_A`. A
   lexicographic best response (first maximise against `q∘β`, then break ties
   against `R_A`) is the `ε → 0` limit in the report's item B. It keeps ties with
   `Σ_a d(a) = 0` and breaks the others. Unlike a fixed `ε`, it does not destroy
   belief-driven robust sensitivity (Example 1, type 3 is strictly optimal at
   different `q`). A pair with `Σ d = 0` and `d ≠ 0` has `d` of both signs, so
   neither action weakly dominates the other: the surviving structural ties are
   exactly the ones unrelated to admissibility. (To verify before use.)
4. **Membership in `F_p(t)` has a dominance dual (proposed; proof sketch).**
   From Lemma 1's layer-cake, `Q_p(t) = {Σ_W λ_W q^W : λ ∈ Δ, λ_T > 0}`.
   Claim: `b ∈ F_p(t)` if and only if there is **no mixed** `σ ∈ Δ(A)` with
   `U_{q^W}(σ) ≥ U_{q^W}(b)` at every window `W` at `t` and `U_p(σ) > U_p(b)`.
   - ⇐ is immediate (`λ_T > 0` makes the difference positive at every class belief).
   - ⇒: in the matrix game `M[a, W] = U_{q^W}(a) − U_{q^W}(b)`, the value is ≥ 0. If
     it is > 0, a strictly dominating `σ` exists. If it is = 0, no optimal column
     strategy puts weight on `T` (otherwise `b` would be optimal at a class belief),
     so Goldman–Tucker strict complementarity gives an optimal `σ` with
     `(σM)_T > 0`.
   - This is Theorem 1(i) with the pure rival replaced by a mixed one: `F_p(t)` is
     the set of actions **not window-dominated**, the analogue of BL's `UD`, with
     "states" replaced by window beliefs and strictness required at `p`. It
     answers the draft's own open question (end of §3; §7). It also delivers the
     report's "present `F_p(t)` as an E-admissible set" as a theorem.
   - Hand-checked on Example 1, type 3 (uniform `p`): `F = {1, 2}` ✓, and on the
     type-5 knife-edge `p₃ + 1.5 p₅ = p₁`: bid 1 is not dominated ✓. Not
     machine-verified: the skill's standing order puts the exact LP solver out of
     scope until the author lifts it.
5. **A BL-style characterisation of mechanisms is already in the draft.** Under
   coverage (every action anchored, anchors singletons), Corollaries 2 and 3
   combine to: *every type is robustly simple if and only if the anchor profile is
   a weak ex-post equilibrium, strict somewhere*. That is a characterisation of
   fully predictable menus under a richness condition, the analogue of
   "strategically simple ⟺ local dictatorship". Note that it is class-free
   (report §3.2).
6. **Treat the belief class as a domain parameter.** BL write "strategically simple
   with respect to U and M" throughout, and Remark 4 shows the classification
   moving when the domain shrinks (single-peaked). The analogue here is nested
   domains: all full-support beliefs ⊃ centred ⊃ distance-symmetric ⊃ {p}. Remark 1
   (monotonicity) is the tool, and draft line ~320 (the symmetric class makes type 3
   simple) is the example. This is a clean way to carry out report item A.
7. **Positioning sentence (BL §6).** BL fix k = 2, use no anchor, and quantify over
   strategic beliefs, which makes them more permissive than level-k. This paper
   fixes the level-k anchor and quantifies over utility beliefs. Cite
   de Clippel–Saran–Serrano (2019) and the other level-k mechanism-design papers
   in BL's footnote 13 (verify the bibliographic details before adding them).
8. **Candour about limitations.** BL flag the failure of the revelation principle
   (Clark–Fudenberg) plainly in one paragraph. The menu-dependence of footnote 6
   (report §3.5) deserves the same treatment.
9. **Exposition.** BL: one motivating example (price cap vs double auction) in about
   two pages, the definitions in two more, "one dimension of simplicity, one
   possible formalisation." Their price cap and this paper's bid cap make a natural
   pairing for the introduction.
10. **Naming.** "Simple" collides with BL, Li (2017) and Pycia–Troyan, which all use
    it for the agent's problem. Since this paper asks the analyst's question,
    consider "determinate" or "pinned" types.
