# AGENTS.md

## Cursor Cloud specific instructions

This repository is the `723eth/723eth` GitHub profile repository. It is not a
deployable software product — there are no long-running services, no databases,
and no web/API/frontend to start.

### What lives here

- `main` branch: a single GitHub profile README file (`👋 Hi, I'm @723eth`).
  Nothing to build or run.
- `cursor/peptides-market-positioning-3357` branch: business/market-research
  Markdown documents plus two standalone Python scripts that render those
  documents to PDF using `reportlab`:
  - `generate_peptides_pdf_report.py`
  - `generate_cosmetics_bodybuilding_business_plan_pdf.py`

### Tooling / how to run

- The only runtime dependency is `reportlab` (installed by the startup update
  script). System Python 3.12 is used; `pip install` defaults to a user install
  in this environment.
- There is no build system, linter config, or test suite in the repo.
- To run the PDF generators, check out the branch that contains them and run the
  script directly, e.g. `python3 generate_peptides_pdf_report.py`.

### Non-obvious gotchas

- Both PDF generator scripts hard-code an absolute output path
  (`OUTPUT_PATH = "/workspace/...pdf"`), so they must be run from an environment
  where `/workspace/` exists and is writable (it does in Cursor Cloud). The
  output PDF is written to `/workspace/` regardless of the current working
  directory.
- `poppler-utils` (`pdftoppm`) is handy for rendering a generated PDF to an
  image for visual verification, but it is not required to run the scripts.
