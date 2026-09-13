# Contributing

The project welcomes mathematical criticism, replay reports, and narrower
counterexamples.  The preferred unit of work is one explicit claim and its
dependency closure.

## For an audit finding

Please include:

- the exact theorem, lemma, certificate field, or source line;
- the first implication you believe is unsupported;
- the command and software version used;
- the observed output and expected output;
- SHA-256 identities for every load-bearing input;
- whether the finding affects integrity, reproducibility, or mathematics.

Do not overwrite historical evidence.  Add a correction package and mark the
older record superseded.

## For a proposed promotion to “proved”

A pull request must update `audit/status.json`, explain every changed gate,
include two independent decisions, update the paper, and pass a clean
extraction replay.  A passing CI check is necessary but not sufficient.
