from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_view, name="landing"),
    path("docs/", views.docs_root_redirect, name="docs_root"),
    path(
        "docs/<slug:section_slug>/<slug:page_slug>/",
        views.doc_view,
        name="doc_page",
    ),
]
