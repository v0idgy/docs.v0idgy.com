from django.db import migrations
from django.utils import timezone


CONTENT = """
<h1>Emmet Crash Course</h1>
<p>Emmet is a code snippets manager for VS Code. It is used to create HTML code faster. Emmet is a must-have tool for any web developer. In VS Code, Emmet is enabled by default. It works only after you have created a new HTML file.</p>
<p>Learn the shortcuts and just press the tab or enter key to get the code you want.</p>
<h2 id="common-shortcuts">Some common Emmet shortcuts</h2>
<ul>
  <li><code>!</code> – Inserts a <code>&lt;!DOCTYPE html&gt;</code> tag</li>
  <li><code>h1</code> – Inserts a <code>&lt;h1&gt;</code> tag</li>
  <li><code>h2</code> – Inserts a <code>&lt;h2&gt;</code> tag</li>
  <li><code>p</code> – Inserts a <code>&lt;p&gt;</code> tag</li>
  <li><code>img</code> – Inserts an <code>&lt;img&gt;</code> tag</li>
  <li><code>a</code> – Inserts an <code>&lt;a&gt;</code> tag</li>
  <li><code>ul</code> – Inserts an <code>&lt;ul&gt;</code> tag</li>
  <li><code>ul&gt;li</code> – Inserts a <code>&lt;li&gt;</code> tag inside an <code>&lt;ul&gt;</code></li>
  <li><code>ul&gt;li&gt;a</code> – Inserts an <code>&lt;a&gt;</code> tag inside a <code>&lt;li&gt;</code> inside an <code>&lt;ul&gt;</code></li>
  <li><code>ul&gt;li*3</code> – Inserts 3 <code>&lt;li&gt;</code> tags inside a <code>&lt;ul&gt;</code></li>
  <li><code>div</code> – Inserts a <code>&lt;div&gt;</code> tag</li>
  <li><code>div&gt;p</code> – Inserts a <code>&lt;p&gt;</code> tag inside a <code>&lt;div&gt;</code></li>
  <li><code>div&gt;p*3</code> – Inserts 3 <code>&lt;p&gt;</code> tags inside a <code>&lt;div&gt;</code></li>
  <li><code>#</code> – Inserts an id attribute</li>
  <li><code>.</code> – Inserts a class attribute</li>
</ul>
<p><strong>Example:</strong></p>
<ul>
  <li><code>#my-id</code> – Inserts an id attribute with the value <code>my-id</code></li>
  <li><code>.my-class</code> – Inserts a class attribute with the value <code>my-class</code></li>
</ul>
<pre><code>div&gt;(header&gt;ul&gt;li*2&gt;a)+footer&gt;p1
</code></pre>
<p>expands into:</p>
<pre><code>&lt;div&gt;
  &lt;header&gt;
    &lt;ul&gt;
      &lt;li&gt;&lt;a href=""&gt;&lt;/a&gt;&lt;/li&gt;
      &lt;li&gt;&lt;a href=""&gt;&lt;/a&gt;&lt;/li&gt;
    &lt;/ul&gt;
  &lt;/header&gt;
  &lt;footer&gt;
    &lt;p&gt;&lt;/p&gt;
  &lt;/footer&gt;
&lt;/div&gt;
</code></pre>
<h2 id="grouping">Grouping</h2>
<p><code>div&gt;(header&gt;ul&gt;li*2&gt;a)+footer&gt;p</code> – Inserts a <code>&lt;div&gt;</code> with a nested structure of header, list items with anchors, then a footer with a paragraph. It can get a bit wild, but you rarely need extreme nesting.</p>
<h2 id="css-shortcuts">CSS shortcuts</h2>
<ul>
  <li><code>style</code> – Inserts a <code>&lt;style&gt;</code> tag</li>
  <li><code>pos</code> – Inserts a <code>position</code> property</li>
  <li><code>pos:absolute</code> – Inserts <code>position: absolute</code></li>
  <li><code>bgc</code> – Inserts a <code>background-color</code> property</li>
  <li><code>bgc:red</code> – Inserts <code>background-color: red</code></li>
  <li><code>ma</code> – Inserts <code>margin: auto</code></li>
</ul>
<h2 id="conclusion">Conclusion</h2>
<p>Emmet is a must-have tool for any web developer. This does not mean you have to learn every single shortcut. Use Emmet to create HTML faster. No one memorizes all shortcuts—we learn them by trial, error, and repeated use.</p>
"""


def add_page(apps, schema_editor):
    Section = apps.get_model("docs", "Section")
    Page = apps.get_model("docs", "Page")
    try:
        section = Section.objects.get(slug="chai-our-html")
    except Section.DoesNotExist:
        return
    Page.objects.update_or_create(
        section=section,
        slug="emmet-crash-course",
        defaults={
            "title": "Emmet Crash Course",
            "order": 3,
            "summary": "Rapid HTML authoring with Emmet shortcuts in VS Code.",
            "content_html": CONTENT,
            "updated_at": timezone.now(),
        },
    )


def remove_page(apps, schema_editor):
    Page = apps.get_model("docs", "Page")
    Page.objects.filter(slug="emmet-crash-course").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("docs", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_page, remove_page),
    ]
