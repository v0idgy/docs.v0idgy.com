from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Section",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("slug", models.SlugField(unique=True)),
                ("order", models.PositiveIntegerField(default=0)),
                ("icon", models.CharField(blank=True, max_length=32)),
                ("description", models.TextField(blank=True)),
            ],
            options={
                "ordering": ["order", "title"],
            },
        ),
        migrations.CreateModel(
            name="Page",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("slug", models.SlugField()),
                ("order", models.PositiveIntegerField(default=0)),
                ("summary", models.CharField(blank=True, max_length=255)),
                ("content_html", models.TextField()),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("section", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="pages", to="docs.section")),
            ],
            options={
                "ordering": ["order", "title"],
            },
        ),
        migrations.AddConstraint(
            model_name="page",
            constraint=models.UniqueConstraint(fields=("section", "slug"), name="unique_page_per_section"),
        ),
    ]
