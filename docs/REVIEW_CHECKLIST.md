# Independent review checklist

This checklist is intended for a hostile, line-by-line review of the research draft before any journal submission or claim of established theorem status.

## 1. Literature and priority

- Verify the exact statement and epsilon range of the Karatsuba short-interval odd-zero theorem from the primary source.
- Verify the classical xi-prime zero-count statements used in the localization.
- Compare the proposed result against Conrey, Rezvyakova, and later work on derivatives of xi and Hardy's Z-function.
- Search MathSciNet, zbMATH, Google Scholar citation chains, and references of the primary papers for prior power-short-interval simple-zero results.

## 2. Local zero count

- Derive the count on `(T,T+H]` from the upstream good-height argument, including arbitrary endpoint adjustment.
- Check that the error is uniform for the fixed power range used in the theorem candidate.
- Check every use of multiplicity versus distinct zero locations.

## 3. Karatsuba-to-xi-prime charge bridge

- Verify the tiling of a `T^theta` interval by intervals to which the printed Karatsuba theorem applies literally.
- Check endpoint losses and the `-1` Rolle loss per tile.
- Verify that the resulting xi-prime critical points have odd analytic multiplicity, not merely distinctness.
- Check normalization by the local xi-prime total count.

## 4. Charge-refined rank-trace lemma

- Re-derive the c=2 inequality directly from the upstream `rank_trace_mult_k_le` theorem.
- Check the bookkeeping identity separating simple, even nonsimple, odd nonsimple, and off-line reflected pairs.
- Verify all coefficients in the proposed `+2Q` improvement.
- Independently check the optional general-c optimization.

## 5. Principal compression

- Confirm that the local matrix is genuinely a principal compression of the upstream matrix.
- Verify that entrywise explicit-formula statements survive unchanged.
- Verify that the zero-side Poisson norm bound can only improve.
- Verify the positive-index/inertia comparison under compression.

## 6. Local first trace

- Rebuild the archimedean Riemann-sum main term for a grid of length H.
- Check the prime contribution and the stated `sqrt(X)/H` relative error.
- Check every replacement of `T` by `T+O(H)`.

## 7. Local second trace and finite-section ends

- Repeat the prime-prime mean-value calculation with interval length H in the diagonal term.
- Check that the off-diagonal Montgomery-Vaughan error is independent of H in the required form.
- Rebuild both one-sided finite-section end estimates after moving the right boundary from 2T to T+H.
- Verify the normalization of the `X/H` and polylogarithmic losses.

## 8. Coefficient freezing and re-expansion

- Verify the exact definition and range of the entry-dependent shift parameter.
- Check the bound `rho_H = O(H/T)` uniformly over the compressed grid.
- Reuse the upstream H1/H2/H3 estimates for each re-expansion coefficient and confirm all powers of log T.
- Retain the non-homogeneous PPUpper end floor; do not silently replace it by a homogeneous bound.
- Check the Frobenius Minkowski sum and the diagonal trace estimate.

## 9. Tail and boundary

- Re-run the upstream tail proof with boundary collar `D0 = H^(1/2)`.
- Verify the precise normalization of the tail perturbation.
- Check the number of zeros in the boundary collar and its effect on simple and odd counts.

## 10. Fixed-profile certificate

- Re-derive the kernel series and every polynomial moment formula.
- Check positivity of the fixed degree-16 profile on the entire interval.
- Verify the sign and geometric bound of the omitted series tail.
- Run the certificate in an independent implementation using exact rational arithmetic.

## 11. Final quantifiers

- Check the ordering of `delta_K`, the inward spectral parameter, `Theta`, and `theta`.
- Confirm that no effective numerical amount below the crossing is claimed.
- Confirm that the final positive proportion may depend on theta.

## 12. Formal verification target

A Lean port should separately formalize the new compression, charge, local first/second trace, coefficient-radius, and final assembly lemmas, then run a complete pinned build and `#print axioms` audit.
