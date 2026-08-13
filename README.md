# xi-prime-short-interval-simple-zeros

**Status: unrefereed research draft.** This repository contains a theorem candidate, proof draft, and exact verification scripts concerning simple critical-line zeros of the derivative of the Riemann xi-function in power-length intervals.

The central candidate claim is that there exists a constant `Theta < 0.51331975984769` such that, for each fixed `theta` with `Theta <= theta < 1`, a positive proportion of zeros of `xi'(s)` in `(T, T + T^theta]` are simple and lie on `Re(s)=1/2`, for all sufficiently large `T`.

This claim has **not** been independently refereed, and the new short-interval localization and charge arguments have **not** been fully formalized in Lean. Nothing in this repository is a proof of the Riemann Hypothesis.

## Contents

- `proof/xi_prime_short_intervals_charge_theorem.md` — full theorem candidate and proof draft.
- `certificates/` — exact-rational crossing certificate and expected output.
- `verification/` — symbolic scaling/charge audit and expected output.
- `STATUS.md` — claim ledger and unresolved validation obligations.
- `PROVENANCE.md` — upstream dependencies, corrections, and research provenance.
- `docs/REVIEW_CHECKLIST.md` — checklist for independent specialist review.

## Reproducibility

The fixed-profile crossing certificate uses only the Python standard library:

```bash
python certificates/xi_prime_fixed_profile_crossing_certificate.py
```

The scaling audit uses SymPy:

```bash
python -m pip install -r requirements.txt
python verification/verify_xi_prime_short_interval_scaling.py
```

The scripts were rerun before initial publication and reproduced the committed text outputs exactly.

## Upstream formal development

The proof draft reuses substantial infrastructure from Anthropic's public Lean repository `anthropics/zeta-23-lean`, pinned at commit `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`. The new local assembly in this repository is not part of that upstream formalization.

## Research disclosure

The mathematical exploration, checking, proof organization, and manuscript preparation were substantially assisted by AI systems. Upstream formalized results, new paper-level arguments, and computational certificates are separated so that they can be independently audited.
