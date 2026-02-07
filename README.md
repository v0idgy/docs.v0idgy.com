# Docs Site (Django + Jinja2)

Recreates the ChaiDocs-inspired docs experience shown in the mockups, using Django 5, Jinja2 templates, and a `docs` app with database-backed sections/pages, client-side theme toggle, search, and on-page TOC. The top navigation is semi-transparent with blur.

## Stack
- Python 3.11+
- Django 5.x
- Jinja2 (via Django backend)
- SQLite (dev)

## Setup
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Database & fixtures
```bash
python manage.py migrate
python manage.py loaddata seed.json
```

## Run dev server
```bash
python manage.py runserver
```
- Landing page: http://127.0.0.1:8000/
- Docs: http://127.0.0.1:8000/docs/ (redirects to first page)

## App structure
- `config/` – project settings, URLs, Jinja2 environment.
- `docs/models.py` – `Section` and `Page` models.
- `docs/views.py` – landing, docs reader, search payload, prev/next links.
- `docs/static/` – CSS, JS (theme, search, TOC), placeholder logo.
- `templates/` – `base.jinja`, `landing.jinja`, `doc_page.jinja`, partials.
- `docs/fixtures/seed.json` – sample sidebar/pages/content.

## Tests
```bash
python manage.py test
```

## Notes
- Theme choice persists in `localStorage` and respects system preference.
- Search is client-side over preloaded JSON (titles, summaries, URLs).
- Semi-transparent nav gains a darker shade on scroll; light theme uses a lighter glass tone.
