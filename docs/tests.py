from django.test import TestCase
from django.urls import reverse
from .models import Section


class DocsTests(TestCase):
    fixtures = ["seed.json"]

    def test_landing_renders(self):
        resp = self.client.get(reverse("landing"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Docs You'll Actually Read")
        self.assertContains(resp, "window.SEARCH_INDEX")

    def test_docs_root_redirects_to_first_page(self):
        resp = self.client.get(reverse("docs_root"))
        self.assertRedirects(
            resp, reverse("doc_page", args=["getting-started", "welcome"])
        )

    def test_doc_page_renders(self):
        resp = self.client.get(reverse("doc_page", args=["html", "html-intro"]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'data-nav="glass"')
        self.assertContains(resp, "On this page")

    def test_404_on_bad_slug(self):
        resp = self.client.get("/docs/unknown/none/")
        self.assertEqual(resp.status_code, 404)

    def test_section_and_page_ordering(self):
        sections = Section.objects.all()
        self.assertEqual(sections.first().slug, "getting-started")
        self.assertEqual(sections.first().pages.first().slug, "welcome")
