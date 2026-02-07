(function () {
  const body = document.getElementById("doc-body");
  const toc = document.getElementById("toc-list");
  if (!body || !toc) return;

  const slugify = (text) =>
    text
      .toLowerCase()
      .trim()
      .replace(/[^a-z0-9\s-]/g, "")
      .replace(/\s+/g, "-");

  const headings = body.querySelectorAll("h2, h3");
  headings.forEach((node) => {
    if (!node.id) {
      node.id = slugify(node.textContent || "section");
    }
    const li = document.createElement("li");
    const link = document.createElement("a");
    link.href = `#${node.id}`;
    link.textContent = node.textContent;
    link.className = "toc-link";
    li.appendChild(link);
    toc.appendChild(li);
  });
})();
