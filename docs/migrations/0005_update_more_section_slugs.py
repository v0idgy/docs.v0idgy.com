from django.db import migrations

def forwards(apps, schema_editor):
    Section = apps.get_model("docs", "Section")
    updates = {
        "chai-our-git": ("Git", "git"),
        "chai-our-sql": ("SQL", "sql"),
        "chai-our-devops": ("DevOps", "devops"),
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
        "git": ("Chai our Git", "chai-our-git"),
        "sql": ("Chai our SQL", "chai-our-sql"),
        "devops": ("Chai our DevOps", "chai-our-devops"),
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
        ("docs", "0004_update_section_slugs"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
