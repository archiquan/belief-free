"""Exact check of review/proposals/prediction_set_dual.tex (Theorem: F = window-undominated set).

Condition (II) is decided exactly: maximise (sigma M)_T over the polytope
{sigma in Delta(A): (sigma M)_W >= 0 for all W} by vertex enumeration in Fractions.
Compared with ripples' grid method, which is sound (every action it returns is
in F) but grid-complete only. So:
  grid action that is dominated  -> REFUTES the theorem
  undominated action the grid misses -> knife-edge, reported, not a refutation
A search, not a proof.
"""
import sys, random
from fractions import Fraction as Fr
from itertools import combinations
sys.path.insert(0, [p for p in __import__('glob').glob('/root/.claude/skills/synced/*/information-ripples-verify')][0])
from ripples import (u_fpa, u_spa, matrix_payoff, anchor_sets, uniform, windows,
                     window_belief, prediction_set, sweep_benchmarks)

def rowval(q, b, t, u, gam, T):
    return sum(q[s] * sum(u(b, a, t) for a in gam[s]) / len(gam[s]) for s in T)

def solve(Mx, rhs):
    n = len(Mx); A = [r[:] + [v] for r, v in zip(Mx, rhs)]
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None: return None
        A[c], A[piv] = A[piv], A[c]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c] / A[c][c]; A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [A[i][n] / A[i][i] for i in range(n)]

def dominated(b, t, A, u, gam, T, p):
    Ws = windows(t, T); qs = [window_belief(W, p, T) for W in Ws]
    iT = next(i for i, W in enumerate(Ws) if len(W) == len(T))
    M = [[rowval(q, a, t, u, gam, T) - rowval(q, b, t, u, gam, T) for q in qs] for a in A]
    n = len(A)
    cons = [[Fr(int(i == a)) for i in range(n)] for a in range(n)] + \
           [[M[a][w] for a in range(n)] for w in range(len(Ws))]
    best = None
    for S in combinations(range(len(cons)), n - 1):
        sol = solve([cons[k] for k in S] + [[Fr(1)] * n], [Fr(0)] * (n - 1) + [Fr(1)])
        if sol is None: continue
        if all(x >= 0 for x in sol) and all(sum(sol[a] * M[a][w] for a in range(n)) >= 0 for w in range(len(Ws))):
            val = sum(sol[a] * M[a][iT] for a in range(n))
            best = val if best is None or val > best else best
    return best is not None and best > 0

def F_dual(t, A, u, gam, T, p):
    return sorted(b for b in A if not dominated(b, t, A, u, gam, T, p))

refute = knife = cases = 0
def compare(label, t, A, u, gam, T, p, show=False):
    global refute, knife, cases
    cases += 1
    if getattr(u, "actions", "x") is None or hasattr(u, "tables"): u.actions = list(A)
    g = prediction_set(t, A, u, T, p, anchors=gam, method="grid")
    d = F_dual(t, A, u, gam, T, p)
    if not set(g) <= set(d):
        refute += 1; print("REFUTED", label, "t", t, "grid", g, "dual", d)
    elif set(g) != set(d):
        knife += 1
        if show or knife <= 5: print("  knife-edge/grid miss:", label, "t", t, "grid", g, "dual", d)
    if show: print(f" {label}, t={t}: dual F = {d} (grid {g})")

T = [1, 3, 5]; pu = uniform(T)
print("=== draft examples (gamma = anchor)")
for A, u, lab in (([0,1,2], u_fpa, "FPA Ex1"), ([0,1], u_fpa, "FPA cap"),
                  (list(range(6)), u_spa, "SPA Ex3"), ([0,2], u_fpa, "FPA tied")):
    an = anchor_sets(A, u, T)
    for t in T: compare(lab, t, A, u, an, T, pu, show=True)
p_edge = {1: Fr(1,2), 3: Fr(1,5), 5: Fr(1,5)}   # p1 = p3 + 1.5 p5
A = [0,1,2]; compare("FPA Ex1 knife-edge p=(1/2,1/5,1/5)", 5, A, u_fpa, anchor_sets(A,u_fpa,T), T, p_edge, show=True)
hedge = matrix_payoff({1: [[1,1,1,1],[3,0,0,1],[0,0,2,0],[0,0,0,0]],
                       2: [[3,-2,0,0],[-2,3,0,0],[1,1,0,0],[-3,-3,3,0]]})
A = [0,1,2,3]; hedge.actions = A; T2 = [1,2]
compare("hedge", 2, A, hedge, anchor_sets(A, hedge, T2), T2, uniform(T2), show=True)

print("=== random instances, non-anchor conjecture profiles")
rng = random.Random(20260924)
for i in range(150):
    nT, nA = rng.choice([2,3,4]), rng.choice([2,3,4])
    Tr = list(range(1, nT+1)); Ar = list(range(nA))
    u = matrix_payoff({t: [[rng.randint(-3,3) for _ in Ar] for _ in Ar] for t in Tr}); u.actions = Ar
    gam = {s: [rng.choice(Ar) for _ in range(rng.choice([1,2,3]))] for s in Tr}
    bench = sweep_benchmarks(Tr, denom=6)
    p = rng.choice(bench)
    for t in Tr: compare(f"rand{i}", t, Ar, u, gam, Tr, p)
print(f"=== {cases} cases: {refute} refutations, {knife} grid misses (knife-edges)")
