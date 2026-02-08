from django.db import migrations

CONTENT = """
<h1>Common HTML Tags</h1>
<div class="callout"><strong>Focus on the essentials.</strong> You don’t need to memorize all HTML. Master core tags and attributes to build solid pages; accessibility and semantics matter the most.</div>
<h2 id="basic-terminology">Basic Terminology</h2>
<ul>
  <li><strong>Tag</strong> – element definition (e.g., <code>&lt;p&gt;</code>, <code>&lt;img&gt;</code>)</li>
  <li><strong>Attribute</strong> – extra info inside a tag (e.g., <code>href</code>, <code>src</code>, <code>alt</code>)</li>
  <li><strong>Element</strong> – full structure (opening tag, content, closing tag)</li>
</ul>
<h2 id="text-content">HTML Tags for Text Content</h2>
<ul>
  <li><code>&lt;p&gt;</code> – Paragraph</li>
  <li><code>&lt;span&gt;</code> – Inline container</li>
  <li><code>&lt;small&gt;</code> – Smaller text</li>
  <li><code>&lt;strong&gt;</code> – Important/semantic bold</li>
  <li><code>&lt;em&gt;</code> – Emphasis/italic</li>
  <li><code>&lt;mark&gt;</code> – Highlight</li>
  <li><code>&lt;br&gt;</code> – Line break</li>
  <li><code>&lt;hr&gt;</code> – Horizontal rule</li>
  <li><code>&lt;code&gt;</code> – Inline code</li>
  <li><code>&lt;pre&gt;</code> – Block code (preformatted)</li>
</ul>
<h2 id="lists">HTML Tags for Lists</h2>
<ul>
  <li><code>&lt;ul&gt;</code> – Unordered list</li>
  <li><code>&lt;ol&gt;</code> – Ordered list</li>
  <li><code>&lt;li&gt;</code> – List item</li>
</ul>
<h2 id="tables">HTML Tags for Tables</h2>
<ul>
  <li><code>&lt;table&gt;</code> – Table container</li>
  <li><code>&lt;thead&gt;</code> – Table header</li>
  <li><code>&lt;tbody&gt;</code> – Table body</li>
  <li><code>&lt;tfoot&gt;</code> – Table footer</li>
  <li><code>&lt;tr&gt;</code> – Table row</li>
  <li><code>&lt;th&gt;</code> – Header cell</li>
  <li><code>&lt;td&gt;</code> – Data cell</li>
</ul>
<h2 id="forms">HTML Tags for Forms</h2>
<ul>
  <li><code>&lt;form&gt;</code> – Form container</li>
  <li><code>&lt;input&gt;</code> – Input field</li>
  <li><code>&lt;label&gt;</code> – Label text</li>
  <li><code>&lt;textarea&gt;</code> – Multi-line text</li>
  <li><code>&lt;select&gt;</code> – Dropdown</li>
  <li><code>&lt;option&gt;</code> – Option inside select</li>
  <li><code>&lt;button&gt;</code> – Button</li>
</ul>
<h2 id="media">HTML Tags for Media</h2>
<ul>
  <li><code>&lt;img&gt;</code> – Image</li>
  <li><code>&lt;source&gt;</code> – Media source (picture/video)</li>
  <li><code>&lt;picture&gt;</code> – Multiple image sources</li>
  <li><code>&lt;video&gt;</code> – Video</li>
  <li><code>&lt;audio&gt;</code> – Audio</li>
</ul>
<h2 id="linking">HTML Tags for Linking and Metadata</h2>
<ul>
  <li><code>&lt;a&gt;</code> – Anchor/link</li>
  <li><code>&lt;link&gt;</code> – External resources (CSS, icons)</li>
  <li><code>&lt;meta&gt;</code> – Page metadata</li>
  <li><code>&lt;script&gt;</code> – Scripts</li>
</ul>
<h3 id="script-variations">Script Tag Variations</h3>
<ul>
  <li><code>&lt;script&gt;</code> – Inline or external script</li>
  <li><code>&lt;script defer&gt;</code> – Executes after parsing</li>
  <li><code>&lt;script async&gt;</code> – Executes as soon as downloaded</li>
  <li><code>&lt;script type="module"&gt;</code> – ES module</li>
</ul>
<h2 id="semantic">Semantic and Meta Content</h2>
<p>Modern HTML5 adds semantic blocks that improve structure and accessibility.</p>
<ul>
  <li><code>&lt;header&gt;</code> – Top of a page/section</li>
  <li><code>&lt;nav&gt;</code> – Navigation links</li>
  <li><code>&lt;main&gt;</code> – Main unique content</li>
  <li><code>&lt;article&gt;</code> – Independent piece of content</li>
  <li><code>&lt;section&gt;</code> – Thematic grouping</li>
  <li><code>&lt;aside&gt;</code> – Side info (related)</li>
  <li><code>&lt;footer&gt;</code> – Footer</li>
  <li><code>&lt;figure&gt;</code> / <code>&lt;figcaption&gt;</code> – Media + caption</li>
  <li><code>&lt;time&gt;</code> – Machine-readable time</li>
</ul>
<h3 id="abbreviations">Abbreviations and inline helpers</h3>
<ul>
  <li><code>&lt;abbr&gt;</code> – Abbreviation expansion</li>
  <li><code>&lt;sup&gt;</code> / <code>&lt;sub&gt;</code> – Superscript / subscript</li>
  <li><code>&lt;cite&gt;</code> – Citation</li>
  <li><code>&lt;q&gt;</code> – Inline quote</li>
</ul>
<h2 id="attributes">Attributes for HTML Tags</h2>
<p>Common global attributes include <code>class</code>, <code>id</code>, <code>title</code>, <code>style</code>, and <code>data-*</code> for custom data. Example:</p>
<pre><code>&lt;a href="/" class="btn" title="Go home"&gt;Home&lt;/a&gt;
&lt;img src="hero.jpg" alt="Descriptive image text" /&gt;
&lt;input type="text" placeholder="Enter your name" /&gt;
&lt;button type="button" disabled&gt;Save&lt;/button&gt;</code></pre>
<h2 id="html5-tags">HTML5 Tags</h2>
<ul>
  <li><code>&lt;dialog&gt;</code> – Modal dialog</li>
  <li><code>&lt;summary&gt;</code> – Summary text for <code>&lt;details&gt;</code></li>
  <li><code>&lt;details&gt;</code> – Expand/collapse</li>
  <li><code>&lt;progress&gt;</code> – Progress indicator</li>
  <li><code>&lt;meter&gt;</code> – Scalar measurement</li>
  <li><code>&lt;template&gt;</code> – Client-side template</li>
  <li><code>&lt;picture&gt;</code> – Responsive images</li>
  <li><code>&lt;source&gt;</code> – Media source item</li>
</ul>
<h2 id="conclusion">Conclusion</h2>
<p>You don’t need every HTML tag to build web pages. Learn the core set first; add more tags as needed for semantics or accessibility.</p>
"""


def forwards(apps, schema_editor):
    Page = apps.get_model("docs", "Page")
    try:
        page = Page.objects.get(slug="common-tags")
    except Page.DoesNotExist:
        return
    page.content_html = CONTENT
    page.save(update_fields=["content_html"])


def backwards(apps, schema_editor):
    # no-op rollback; keep updated content
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("docs", "0002_add_emmet_page"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
