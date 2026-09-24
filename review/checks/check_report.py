"""Exact checks of the referee report's claims (Report_quan_JMP_20260923.pdf).

Simplicity is decided by the window test of Theorem 1(i), which the report
verified and which is exact: no belief sampling. All arithmetic in Fractions.
"""
import sys
from fractions import Fraction as Fr
from itertools import product
sys.path.insert(0, "/root/.claude/skills/synced/aeec231c-7ae6-414d-9f23-c1bf49901514_5fd4a864-2038-402d-90d8-51e0917dbc36/information-ripples-verify")
from ripples import u_fpa, u_spa, anchor_sets, uniform, sweep_benchmarks, windows

def rows(A, u, T, eps=Fr(0)):
    """row[t][b][s]: payoff of b for type t against believed type s, under the
    anchor perturbed toward the uniform reference: (1-eps) beta(s) + eps R_A."""
    anch = anchor_sets(A, u, T)
    R = {}
    for t in T:
        R[t] = {b: {s: (1 - eps) * sum(u(b, a, t) for a in anch[s]) / len(anch[s])
                        + eps * sum(u(b, a, t) for a in A) / len(A) for s in T} for b in A}
    return anch, R

def simple_at(t, A, row, T, p):
    """Theorem 1(i): returns the witnessing action or None."""
    for b in A:
        ok = True
        for bp in A:
            if bp == b: continue
            dl = {s: row[b][s] - row[bp][s] for s in T}
            for W in windows(t, T):
                v = sum(p[s] * dl[s] for s in W)
                if v < 0 or (v == 0 and len(W) == len(T)):
                    ok = False; break
            if not ok: break
        if ok: return b
    return None

def P(A, u, T, p, eps=Fr(0)):
    _, R = rows(A, u, T, eps)
    return sum(p[t] for t in T if simple_at(t, A, R[t], T, p) is not None)

def say(*a): print(*a)

T = [1, 3, 5]; pu = uniform(T); bench = sweep_benchmarks(T, denom=20)

say("=== 1. Footnote 6 (concluding section), second witness: FPA T={2,4,6}")
for A in ([0, 1, 3], [1, 3]):
    T2 = [2, 4, 6]; anch, R = rows(A, u_fpa, T2)
    sums = {t: {b: sum(u_fpa(b, a, t) for a in A) for b in A} for t in T2}
    say(f" A={A}: reference sums {sums}")
    say(f"   anchors {anch}; P(uniform) = {P(A, u_fpa, T2, uniform(T2))}")
say("=== 1b. Footnote 6, first witness: FPA T={1,6}")
for A in ([0, 3, 4], [0, 4]):
    T2 = [1, 6]; anch, R = rows(A, u_fpa, T2)
    say(f" A={A}: anchors {anch}; P(uniform) = {P(A, u_fpa, T2, uniform(T2))}")

say("=== 2. Item B: perturbed anchors, eps = 1/100")
e = Fr(1, 100)
say(f" SPA A=0..5, T={T}: P(uniform) eps=0 -> {P(list(range(6)), u_spa, T, pu)}, eps=1/100 -> {P(list(range(6)), u_spa, T, pu, e)}")
# B(iii) over all grids in {0..8} containing T, many benchmarks
fails = 0; n = 0
extra = [x for x in range(9) if x not in T]
for k in range(len(extra) + 1):
    for mask in product([0, 1], repeat=len(extra)):
        A = sorted(T + [x for x, m in zip(extra, mask) if m])
        for p in bench[::7]:
            n += 1
            if P(A, u_spa, T, p, e) != 1: fails += 1
    break
say(f" B(iii) SPA, every grid T<=A<={{0..8}}, {len(bench[::7])} benchmarks: {fails} failures of P=1 in {n} cases (a search)")
# B(ii) nuance: FPA Example 1, type 3 robust sensitivity under eps
A = [0, 1, 2]
sens = [p for p in bench if simple_at(3, A, rows(A, u_fpa, T, e)[1][3], T, p) is None]
say(f" FPA Ex.1 type 3 at eps=1/100: sensitive at {len(sens)}/{len(bench)} benchmarks")
simp = [p for p in bench if simple_at(3, A, rows(A, u_fpa, T, e)[1][3], T, p) is not None]
if simp: say("   e.g. simple at p =", {s: str(v) for s, v in simp[0].items()})
# Example 4 (tied anchor) under eps
A = [0, 2]
sens = [p for p in bench if simple_at(3, A, rows(A, u_fpa, T, e)[1][3], T, p) is None]
say(f" FPA A={{0,2}} type 3 at eps=1/100: sensitive at {len(sens)}/{len(bench)} benchmarks")
say(f"   sum_a d(a) for bid0 vs bid2, type 3: {sum(u_fpa(0,a,3)-u_fpa(2,a,3) for a in A)}")

say("=== 3. Rationalizability, Example 1, type 1 (FPA A={0,1,2})")
A = [0, 1, 2]
say(f" u(b,a;1) rows: " + str({b: [str(u_fpa(b, a, 1)) for a in A] for b in A}))
# iterated deletion of actions never a best response to any belief over surviving opponent actions
S = {t: set(A) for t in T}
N = 30
grid = [(Fr(i, N), Fr(j, N), Fr(N - i - j, N)) for i in range(N + 1) for j in range(N + 1 - i)]
for it in range(5):
    opp = sorted(set().union(*S.values()))
    new = {}
    for t in T:
        keep = set()
        for w in grid:
            bel = dict(zip(A, w))
            if any(bel[a] > 0 for a in A if a not in opp): continue
            vals = {b: sum(bel[a] * u_fpa(b, a, t) for a in A) for b in A}
            m = max(vals.values()); keep |= {b for b in A if vals[b] == m}
        new[t] = keep & S[t]
    if new == S: break
    S = new
say(f" rationalizable sets (grid search over beliefs, denom {N}): {S}")
say(f" paper's F_p (uniform): 1:[0], 3:[1,2], 5:[2]")

say("=== 2b. Item B(ii) nuance: is FPA Ex.1 type 3 still sensitive at EVERY benchmark for fixed eps?")
A = [0, 1, 2]
for p5 in (Fr(1, 20), Fr(1, 100), Fr(1, 1000)):
    p = {1: (1 - p5) / 2, 3: (1 - p5) / 2, 5: p5}
    w = simple_at(3, A, rows(A, u_fpa, T, e)[1][3], T, p)
    say(f" eps=1/100, p=(({1-p5}/2),({1-p5}/2),{p5}): type 3 {'simple, bids ' + str(w) if w is not None else 'sensitive'}")
