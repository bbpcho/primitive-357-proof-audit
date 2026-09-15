# Exceptional-sector citation review

Reviewed 15 September 2026 against `work/pre_submission_revision_2026_09_15/repository/paper/manuscript.tex`, especially lines 1007–1015, 1041–1042 and 1740–1762. Read-only review: no manuscript or released evidence was changed.

## Conclusions

1. **Do not replace Breuil–Diamond with a different level-lowering citation.** PVT explicitly cites that paper in the proof of the theorem actually used here. The existing bibliographic identity is correct; issue number and DOI can be added.
2. **Retain PVT Theorem 7.8 as the direct imported theorem.** A direct application of Breuil–Diamond has additional hypotheses and would require a separate argument. This is not a harmless citation substitution.
3. **Complete the Dembélé–Voight publication details.** “Author's version” is an inadequate stand-alone bibliographic description of a published chapter. Preserve an explicit link to the corrected authors' version, whose Theorem 3.9 and §4 were actually checked.

## PVT and Breuil–Diamond

In the exact PVT v1 PDF, printed/PDF page 32, §7.2 sets up the specialized plus representation and Theorem 7.8 gives the four possible levels under residual irreducibility. Its proof cites Theorem 2.4 and BCDF25, Theorem 3.13, for modularity with trivial Nebentypus, then explicitly cites **[BD14]** for Hilbert level lowering. PVT's bibliography identifies [BD14] as Breuil–Diamond, *Ann. Sci. Éc. Norm. Supér.* (4) 47(5) (2014), 905–974. This agrees with the current manuscript's entry. [PVT v1, Theorem 7.8 and bibliography](https://arxiv.org/pdf/2512.17845v1).

I also reread page 32 from the archived local file `work/v3_audit/extracted/2026-09-13_primitive_357_dependency_closed_release_v3/repository/references/Pacetti_Villagra_Torcomian_2512.17845v1.pdf`. The source's actual citation is not inferred from an audit summary or from similarity between paper titles.

The manuscript's substitution `(a,b,c)=(X,-Z,Y)`, with `p=7`, gives the PVT equation `a^5+b^7+c^3=0` from `X^5+Y^3=Z^7`. It supplies the primitive nontrivial specialization in the stated irreducible branch. Nothing in Theorem 7.8 excludes 7; the exceptional-prime list in PVT's headline elimination theorem is a different assertion and is not the imported input here.

The published Breuil–Diamond paper contains Theorem 3.2.2 at printed page 937. It is a modular lifting result with prescribed local conditions, including irreducibility after restriction to the cyclotomic extension `F(ζ_p)`, beyond modularity and `p>2`. Its special extra restriction at `p=5` is irrelevant here, but the cyclotomic-restriction condition cannot be discarded. Its title concerns a broader application and does not make it the wrong source for the result used within PVT. [Published Breuil–Diamond PDF, Theorem 3.2.2](https://www.numdam.org/item/10.24033/asens.2230.pdf).

PVT cites the paper [BD14] without specifying a theorem number at that step. Accordingly, do not write that PVT explicitly cites “Theorem 3.2.2” unless distinguishing that identification from their actual printed citation. This review verifies the citation chain and the already selected specialized theorem; it does not replace the imported PVT theorem with a new independent proof from Breuil–Diamond.

### Exact proposed edits

The direct PVT citation at lines 1007–1008 should remain. To make the currently uncited Breuil–Diamond bibliography entry's role explicit, the following is a precise optional replacement for the explanatory sentence beginning “This theorem packages…”:

```latex
This specialized theorem incorporates modularity, the local conductor
calculation, and Hilbert level lowering; its proof cites
\cite{BreuilDiamond} for the latter. It gives a parallel-weight-two
Hilbert newform over $F$, with trivial Nebentypus,
whose residual representation is $\bar\rho_7$ and whose level is one of
```

This preserves the theorem interface and leaves the following displayed four levels unchanged.

Complete the Breuil–Diamond entry as follows (the existing title, year and page range are retained). The publication record confirms the issue and DOI. [Journal publication record](https://www.numdam.org/articles/10.24033/asens.2230/).

```latex
\bibitem{BreuilDiamond}
C.~Breuil and F.~Diamond,
\emph{Formes modulaires de Hilbert modulo $p$ et valeurs d'extensions entre
caract\`eres galoisiens},
Ann. Sci. \'{E}c. Norm. Sup\'{e}r. (4) \textbf{47} (2014), no.~5, 905--974,
\href{https://doi.org/10.24033/asens.2230}{doi:10.24033/asens.2230}.
```

Since the audit uses the frozen v1 statement, a useful additional precision is to change the PVT entry's final two lines to:

```latex
arXiv:2512.17845v1 (2025),
\url{https://arxiv.org/abs/2512.17845v1}.
```

## Dembélé–Voight

The publisher identifies the chapter as Lassina Dembélé and John Voight, *Explicit Methods for Hilbert Modular Forms*, in *Elliptic Curves, Hilbert Modular Forms and Galois Deformations*, Advanced Courses in Mathematics—CRM Barcelona, Birkhäuser, Basel, 2013, pp. 135–198; chapter DOI **10.1007/978-3-0348-0618-3_4**. Its publication date is 20 May 2013. [Publisher chapter record](https://link.springer.com/chapter/10.1007/978-3-0348-0618-3_4), [publisher contents and page range](https://link.springer.com/book/10.1007/978-3-0348-0618-3).

In the corrected authors' PDF dated 30 May 2024, Theorem 3.9 is the Hecke-equivariant Eichler–Shimizu–Jacquet–Langlands embedding, with image new at the finite discriminant primes. The following discussion explicitly gives the full-space isomorphism for discriminant `(1)`. Section 4 is the definite method under strict class number one. These are the asserted interfaces in the present paper. Theorem 3.9 and §4 also have those labels in the authors' arXiv v2. [Corrected authors' PDF, Theorem 3.9 and §4](https://jvoight.github.io/articles/hmf-crm-bcn-053024.pdf), [arXiv v2](https://arxiv.org/pdf/1010.5727v2).

The authors' 30 May 2024 errata identify the published chapter and do not amend Theorem 3.9. Relevant nearby corrections add the condition that the Hecke prime not divide `DN` and correct a stabilizer-symbol typo on published page 148. Here the finite quaternion discriminant is 1 and the auxiliary primes avoid the level, so neither changes the adopted argument. [Authors' errata](https://jvoight.github.io/articles/hmf-crm-bcn-errata.pdf).

**Numbering verification boundary.** Theorem 3.9 and §4 are directly checked in both accessible primary author versions. The publisher's full chapter request redirects to an access-restricted landing page, so this review does not claim to have independently inspected Theorem 3.9 in the typeset 2013 chapter. The numbering agrees across the accessible versions, and the errata disclose no change to it, but that is not a substitute for direct inspection of the printed theorem. This limited bibliographic uncertainty is eliminated from the proposed citation by explicitly identifying the corrected author version used for the locator. Do not invent a published theorem page number.

### Exact proposed replacement bibliography entry

```latex
\bibitem{DembeleVoight}
L.~Demb\'el\'e and J.~Voight,
\emph{Explicit methods for Hilbert modular forms},
in \emph{Elliptic Curves, Hilbert Modular Forms and Galois Deformations},
Advanced Courses in Mathematics--CRM Barcelona,
Birkh\"auser, Basel, 2013, 135--198,
\href{https://doi.org/10.1007/978-3-0348-0618-3_4}
{doi:10.1007/978-3-0348-0618-3\_4}.
Theorem~3.9 and \S4 are cited from the
\href{https://jvoight.github.io/articles/hmf-crm-bcn-053024.pdf}
{corrected authors' version of 30 May 2024}.
```

The existing body locator `\cite[Theorem~3.9 and \S4]{DembeleVoight}` may then remain unchanged. This supplies the genuine published reference and preserves a checked, accessible source for the exact theorem numbering, without calling the entire work unpublished or silently substituting a different Jacquet–Langlands statement.
