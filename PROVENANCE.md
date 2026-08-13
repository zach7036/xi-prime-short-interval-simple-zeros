# Provenance and research disclosure

This file records where the mathematical ingredients in this repository come from and which parts are new, adapted, computational, or still awaiting external review.

## Upstream formal source

A substantial portion of the analytic infrastructure comes from the public repository:

- `anthropics/zeta-23-lean`
- pinned commit: `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`

The upstream tree contains formal developments for, among other things, zeros of xi-prime, zero counting, explicit formulae, coefficient families, prime-side estimates, rank-trace inequalities, zero-side multiplicity bookkeeping, and tail estimates.

The short-interval localization and odd-charge assembly developed in this repository are **not** claimed to be present in or endorsed by the upstream repository.

## Primary literature inputs

The research draft relies on classical results including work of A. A. Karatsuba on odd-order critical-line zeros of zeta in short intervals, B. Conrey on zeros of derivatives of the Riemann xi-function, and I. S. Rezvyakova on zeros and simple zeros of derivatives of xi.

A complete publication manuscript should include full bibliographic verification and a priority search using MathSciNet, zbMATH, citation chains, and related literature.

## New research ideas developed here

The project explores two main additions to the upstream machinery:

1. retaining the extra multiplicity budget contributed by odd nonsimple critical-line zeros in a multiplicity-aware rank-trace inequality; and
2. localizing the existing Gabor/explicit-formula construction by principal compression when the Dirichlet-polynomial scale is strictly shorter than the height interval.

The repository also includes a fixed-profile exact-rational arithmetic certificate and symbolic scaling checks. These computational artifacts verify only the calculations encoded in the scripts; they do not independently establish the analytic short-interval theorem candidate.

## Corrections made during the research process

The research record contains several corrections that should be preserved in any public account:

- the Karatsuba input should be invoked at an exponent literally covered by the printed epsilon range, rather than casually substituted at 1/3;
- the released PPUpper estimate contains a non-homogeneous end term and should not be described as perfectly homogeneous;
- the numerical crossing near 0.5133197598 should be separated from the analytic theorem candidate and supported by a reproducible fixed-profile arithmetic certificate;
- no exact numerical improvement below the crossing is currently claimed because the positive odd-zero density constant is used non-effectively;
- none of the work proves the Riemann Hypothesis.

## AI assistance

The mathematical exploration, derivation, checking, source comparison, proof organization, manuscript drafting, and repository preparation were substantially assisted by AI systems, including OpenAI models. AI-generated mathematical arguments can contain subtle errors. The project should therefore be independently checked before submission or public claims of theorem status.

## Authorship

This repository is maintained under the GitHub account `zach7036`. No statement in this file is intended to resolve formal paper authorship, credit allocation, or licensing. Those decisions should be made explicitly before journal submission or archival publication.
