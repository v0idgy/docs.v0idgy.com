from django.db import models
from django.urls import reverse


class Section(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)
    icon = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.title


class Page(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="pages"
    )
    title = models.CharField(max_length=160)
    slug = models.SlugField()
    order = models.PositiveIntegerField(default=0)
    summary = models.CharField(max_length=255, blank=True)
    content_html = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]
        constraints = [
            models.UniqueConstraint(
                fields=["section", "slug"], name="unique_page_per_section"
            )
        ]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.section.title} / {self.title}"

    def get_absolute_url(self):
        return reverse("doc_page", args=[self.section.slug, self.slug])
