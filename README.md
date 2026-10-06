# Abdul Rahim — portfolio and resumes

Finalized black-first static portfolio, plus two one-page AI and backend/SWE PDF resumes.

## Preview

The finalized homepage is `index.html`. Monochrome comparison previews remain at `portfolio-white.html` and `portfolio-black.html`.
Serve the workspace and open either file; the White/Black controls compare the
same layout and content and retain the current section anchor. The homepage uses the black palette without comparison controls.

Rebuild the homepage and both previews with `python scripts/build_minimal_portfolios.py`. Their shared
layout is in `templates/portfolio-minimal.html`, with CSS and lightweight browser
enhancements in `assets/portfolio-minimal.css` and `assets/portfolio-minimal.js`.
Project-specific website wording lives in the builder; professional facts and
coding profiles come from the content files.

Open `index.html`, or serve this folder with `python -m http.server 8765 --bind 127.0.0.1` and visit `http://127.0.0.1:8765`.
The homepage includes the AI resume download. Content and navigation work without JavaScript.

## Edit and rebuild

- `content/profile.json` is the shared content source for both resumes and the portfolio.
- `templates/portfolio-minimal.html` owns the current website layout.
- `CLAIMS_REVIEW.md` records the evidence, excluded claims, and outstanding factual checks.

Run `python scripts/build_minimal_portfolios.py` after content or website template changes. The older `build_portfolio.py` generates the previous design and should not be used for the finalized homepage.
Run `python scripts/build_resumes.py` in an environment with `reportlab` and `pypdf` after resume content changes. It writes both PDFs and editable Markdown copies under `output/pdf/` and requires each PDF to fit on one page.

The current Codex bundled interpreter is:

```sh
/Users/abdulrahim/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_resumes.py
```

The original `/Users/abdulrahim/Resume` files and existing alternate portfolio designs are untouched. `archive/` preserves the former main portfolio and PDF. The root `resume.pdf` is an alias copy of the new AI resume for existing links; update that copy after rebuilding.

## Verification (6 October 2026)

Both PDFs fit on one page, have selectable text and working PDF link annotations, and were visually inspected with Poppler rendering. Portfolio focus switching, project reordering, disclosure expansion, resume highlighting, and mobile overflow were checked in the browser. Project descriptions were checked against local source; project runtime benchmarks and historical business metrics were not independently reproduced.

The monochrome candidates were simplified after browser feedback: text-only
project rows with purpose and implementation contributions for Nemotron, PDF
RAG, and pi-mlx-vision; no form-automation project
or illustrations; full experience and skills; one AI resume link; and a compact
contact row. Coding achievements remain in the resumes, without a separate
portfolio section. Both palettes
were visually checked at desktop and mobile widths, including 320px with no
horizontal overflow. Theme links preserve the section anchor, the AI resume
points to the existing PDF, and browser console checks showed no errors.
Hover is restricted to fine pointers, with reduced-motion support. Contact
wraps naturally on narrow phones. No deployment was performed.
