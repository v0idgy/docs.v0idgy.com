from django.templatetags.static import static
from django.urls import reverse
from django.conf import settings
from jinja2 import Environment


def environment(**options):
    """Configure Jinja2 environment with Django helpers."""
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
            "settings": settings,
        }
    )
    return env
