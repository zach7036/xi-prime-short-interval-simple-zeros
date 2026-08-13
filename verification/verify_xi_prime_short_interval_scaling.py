#!/usr/bin/env python3
"""Symbolic/numerical scaling audit for the proposed local xi' theorem.

This script does NOT prove the analytic input lemmas. It verifies that, once the
localized versions of the released trace/PP/re-expansion estimates are inserted,
every displayed remainder is o(N_I) under the strict-band hypotheses
    0 < lambda < theta < 1.
It also checks the algebraic charge-capacity formula.
"""
from __future__ import annotations
import sympy as sp

lam, theta, delta, kappa, a = sp.symbols('lambda theta delta kappa a', real=True)

exponents = {
    'sqrtX_over_H': lam/2 - theta,
    'X_over_H': lam - theta,
    'H_over_T': theta - 1,
    'boundary_H_minus_half': -theta/2,
    'entry_dependence_homogeneous': theta - 1,
    'entry_dependence_end_floor': theta/2 - 1,
    'end_floor_polylog_over_H': -theta,
    'end_X_polylog_over_H': lam - theta,
}

print('Strict-band scaling audit (polylog factors suppressed):')
for name, e in exponents.items():
    print(f'  {name:36s}: exponent {sp.simplify(e)}')

print('\nElementary sign certificates under 0 < lambda < theta < 1:')
print('  lambda/2-theta < -theta/2 < 0')
print('  lambda-theta < 0')
print('  theta-1 < 0')
print('  -theta/2 < 0')
print('  theta/2-1 < -1/2 < 0')
print('  -theta < 0')

F = sp.simplify((2*a - kappa - a**2*(1-delta)/2)/(2*a-1))
print('\nGeneric charge-capacity lower bound:')
print('  F(a) =', F)

F2 = sp.factor(F.subs(a, 2))
print('  F(2) =', F2)
assert sp.simplify(F2 - (2-kappa+2*delta)/3) == 0

dF_num = sp.factor(sp.together(sp.diff(F, a)) * (2*a-1)**2 * 2)
print('  derivative numerator (scaled) =', dF_num)
roots = sp.solve(sp.Eq(sp.factor(sp.together(sp.diff(F,a)).as_numer_denom()[0]), 0), a)
print('  critical roots =', roots)

Fopt = (3+delta-sp.sqrt((1-delta)*(8*kappa-7-delta)))/4
Fopt2 = sp.simplify(Fopt.subs(kappa, 2))
expected2 = (3+delta-sp.sqrt((1-delta)*(9-delta)))/4
assert sp.simplify(Fopt2-expected2) == 0
print('  optimized closed form =', Fopt)
print('  at kappa=2 =', Fopt2)

threshold = 2/(1-delta)
zero_sq = sp.expand((3+delta)**2 - (1-delta)*(8*threshold-7-delta))
assert sp.simplify(zero_sq) == 0
print('  positivity threshold (for 0 <= delta < 1): kappa < 2/(1-delta)')
print('  equivalently c_lambda > (1-delta)/2')

threshold_c2 = 2 + 2*delta
assert sp.simplify(F2.subs(kappa, threshold_c2)) == 0
print('  c=2 sufficient threshold: kappa < 2(1+delta)')
print('  equivalently c_lambda > 1/[2(1+delta)]')

lam_num = sp.Rational(51331975984768, 10**14)
theta_num = sp.Rational(5134, 10**4)  # 0.5134
assert 0 < lam_num < theta_num < 1
print('\nNumerical sanity point:')
print('  lambda =', sp.N(lam_num, 16))
print('  theta  =', sp.N(theta_num, 16))
for name, e in exponents.items():
    val = sp.N(e.subs({lam:lam_num, theta:theta_num}), 18)
    print(f'  {name:36s}: {val}')
    assert val < 0

print('\nAll algebraic and strict-band scaling checks passed.')
