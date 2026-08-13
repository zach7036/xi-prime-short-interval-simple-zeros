# Research status

Last updated: August 13, 2026.

This repository is an **unrefereed research draft**. The central short-interval statement is a theorem candidate, not an established result.

## Claim ledger

### Upstream results used as established inputs

The project relies on published analytic number theory and on the public Lean development `anthropics/zeta-23-lean` at commit `3635e74826a4c1fcece7d1cd2b6fa75e43a00510` for substantial global xi-prime infrastructure, including zero configuration facts, zero counting, explicit-formula machinery, coefficient estimates, rank-trace inequalities, prime-side moments, and tail bounds.

### Independently checked components in this project

- The odd-Rolle bridge from consecutive odd-multiplicity zeros of the real xi-function to odd-multiplicity critical-line zeros of its derivative is elementary and has been rederived independently.
- The new multiplicity bookkeeping that adds odd-zero "charge" to the released c=2 rank-trace inequality has been checked algebraically.
- The fixed degree-16 polynomial profile is positive on its full interval by an exact rational lower bound.
- The fixed-profile crossing certificate is exact-rational and reproducible.
- The symbolic scaling audit verifies the stated exponent inequalities and charge identities.
- Both verification scripts reproduce their committed output files exactly in the development environment.

### Paper-level but not independently refereed

- Local xi-prime zero-count repackaging for intervals of length H = T^theta.
- Principal-compression localization of the released Gabor matrix.
- Local first-trace and second-trace assembly in the strict band X = o(H).
- Local finite-section/end estimates.
- Localized coefficient re-expansion with the non-homogeneous PPUpper end floor retained.
- Final assembly combining local traces with Karatsuba charge.

### Not yet completed

- Independent line-by-line review by an analytic number theorist.
- Complete priority search in MathSciNet/zbMATH and citation chains.
- Lean formalization of the new local-compression, charge, local prime-side, and coefficient-freezing seams.
- A pinned formal build and `#print axioms` audit of those new lemmas.
- Peer review or journal acceptance.

## Central candidate claim

The draft argues that there exists a constant

`Theta < 0.51331975984769`

such that for every fixed `theta` with `Theta <= theta < 1`, a positive proportion of zeros of `xi'(s)` in `(T, T + T^theta]` are simple and lie on the critical line for all sufficiently large `T`.

The amount by which `Theta` is below the displayed crossing, and the resulting positive proportion, are currently non-effective because the Karatsuba density constant is used only qualitatively.

## Claims that are explicitly *not* made

- This is not a proof of the Riemann Hypothesis.
- This is not a Density Hypothesis theorem.
- The repository does not claim that every zero of xi-prime is on the critical line.
- The central short-interval claim is not presented as peer reviewed or Lean verified.
- The literature priority claim is provisional.

## Recommended citation language before external review

Use wording such as:

> "An unrefereed research draft proposes a positive-proportion theorem for simple critical-line zeros of xi-prime in power-length intervals below exponent 0.51332, supported by exact computational certificates and a paper-level localization argument."

Do not describe the project as having solved RH or as an established theorem until independent review has been completed.
