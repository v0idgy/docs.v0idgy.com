import json
from typing import List, Tuple
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Page, Section


def _prefetched_sections():
    """Return sections with ordered pages for sidebar/search."""
    return (
        Section.objects.all()
        .order_by("order", "title")
        .prefetch_related(
            Prefetch("pages", queryset=Page.objects.all().order_by("order", "title"))
        )
    )


def _search_payload(sections) -> List[dict]:
    payload = []
    for section in sections:
        for page in section.pages.all():
            payload.append(
                {
                    "title": page.title,
                    "section": section.title,
                    "summary": page.summary,
                    "url": page.get_absolute_url(),
                }
            )
    return payload


def _page_sequence(sections) -> List[Page]:
    ordered: List[Page] = []
    for section in sections:
        ordered.extend(list(section.pages.all()))
    return ordered


def _adjacent_pages(target: Page, sequence: List[Page]) -> Tuple[Page | None, Page | None]:
    try:
        idx = sequence.index(target)
    except ValueError:
        return None, None
    prev_page = sequence[idx - 1] if idx > 0 else None
    next_page = sequence[idx + 1] if idx < len(sequence) - 1 else None
    return prev_page, next_page


def docs_root_redirect(request):
    first = (
        Page.objects.select_related("section")
        .order_by("section__order", "order", "title")
        .first()
    )
    if not first:
        return redirect("landing")
    return redirect(first.get_absolute_url())


def landing_view(request):
    sections = _prefetched_sections()
    search_data = _search_payload(sections)
    return render(
        request,
        "landing.jinja",
        {
            "sections": sections,
            "search_data_json": json.dumps(search_data),
        },
    )


def doc_view(request, section_slug: str | None = None, page_slug: str | None = None):
    sections = _prefetched_sections()
    if not section_slug or not page_slug:
        return docs_root_redirect(request)

    section = get_object_or_404(Section, slug=section_slug)
    page = get_object_or_404(Page, section=section, slug=page_slug)

    sequence = _page_sequence(sections)
    prev_page, next_page = _adjacent_pages(page, sequence)
    search_data = _search_payload(sections)

    return render(
        request,
        "doc_page.jinja",
        {
            "sections": sections,
            "section": section,
            "page": page,
            "search_data_json": json.dumps(search_data),
            "prev_page": prev_page,
            "next_page": next_page,
        },
    )
