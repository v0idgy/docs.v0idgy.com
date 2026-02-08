from django.db import migrations

def forwards(apps, schema_editor):
    Section = apps.get_model("docs", "Section")
    updates = {
        "chai-our-html": ("HTML", "html"),
        "chai-our-cpp": ("C++", "cpp"),
        "chai-our-django": ("Django", "django"),
    }
    for old_slug, (title, new_slug) in updates.items():
        try:
            section = Section.objects.get(slug=old_slug)
            section.title = title
            section.slug = new_slug
            section.save(update_fields=["title", "slug"])
        except Section.DoesNotExist:
            continue


def backwards(apps, schema_editor):
    Section = apps.get_model("docs", "Section")
    updates = {
        "html": ("Chai our HTML", "chai-our-html"),
        "cpp": ("Chai our C++", "chai-our-cpp"),
        "django": ("Chai our Django", "chai-our-django"),
    }
    for old_slug, (title, new_slug) in updates.items():
        try:
            section = Section.objects.get(slug=old_slug)
            section.title = title
            section.slug = new_slug
            section.save(update_fields=["title", "slug"])
        except Section.DoesNotExist:
            continue


class Migration(migrations.Migration):
    dependencies = [
        ("docs", "0003_update_common_tags_content"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
