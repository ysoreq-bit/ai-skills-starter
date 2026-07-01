# Tests

Run locally with free tools:

```bash
python -m unittest discover -s tests -v
python scripts/validate.py tests/fixtures/valid-layout.tex
python scripts/validate.py tests/fixtures/page-break-in-minipage.tex
python scripts/validate.py --strict tests/fixtures/manual-spacing.tex
```

The structural validator complements compilation and visual review; it does not replace them.
