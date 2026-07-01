# Optional Free Tool Catalog

Tools are optional dependencies, not automatic defaults. Pilot them on representative files before adding them to a standard workflow.

## MarkItDown

- **Source:** `microsoft/markitdown`
- **License:** MIT
- **Status:** Pilot
- **Best for:** Quick conversion of common documents and structured files into Markdown for analysis.
- **Limit:** It targets machine-readable extraction, not faithful page design.
- **Use rule:** Start here when layout is not the deliverable.

## Docling

- **Source:** `docling-project/docling`
- **License:** MIT
- **Status:** Pilot
- **Best for:** Complex PDFs, reading order, tables, formulas, OCR, charts, and structured local parsing.
- **Limit:** Heavier installation and processing than lightweight converters.
- **Use rule:** Escalate when structure or multimodal page content matters.

## Pandoc

- **Source:** `jgm/pandoc`
- **License:** GPL-2.0-or-later
- **Status:** Optional tool
- **Best for:** Mature format conversion, templates, filters, bibliographies, and controlled transformations.
- **Limit:** Conversion is not proof of visual fidelity.
- **Use rule:** Use for transformations, not one-to-one reconstruction.

## TexLab

- **Source:** `latex-lsp/texlab`
- **License:** GPL-3.0
- **Status:** Pilot
- **Best for:** LaTeX editor diagnostics, cross-file navigation, dependency awareness, build and forward-search integration.
- **Limit:** It does not replace compilation or rendered-output review.

## diff-pdf

- **Source:** `vslavik/diff-pdf`
- **License:** GPL-2.0
- **Status:** Cautious pilot
- **Best for:** Comparing two rendered PDFs and producing highlighted visual differences.
- **Limit:** The upstream repository reports limited active development.
- **Use rule:** Compare with a maintained render-to-image pipeline before making it required.

## Document-input ladder

1. Existing clean text or Markdown.
2. Built-in extraction available in the current environment.
3. Lightweight conversion for ordinary documents.
4. Advanced parsing for complex layout, OCR, tables, formulas, or charts.
5. Direct visual reconstruction only when page fidelity is itself the goal.
