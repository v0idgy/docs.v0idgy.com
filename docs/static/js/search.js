(function () {
  const input = document.getElementById("search-input");
  const resultsEl = document.getElementById("search-results");
  const templateEl = document.getElementById("search-result-item-template");
  const data = Array.isArray(window.SEARCH_INDEX) ? window.SEARCH_INDEX : [];

  if (!input || !resultsEl || !templateEl) return;

  const render = (items) => {
    resultsEl.innerHTML = "";
    if (!items.length) {
      resultsEl.style.display = "none";
      return;
    }
    items.slice(0, 8).forEach((item) => {
      const wrapper = document.createElement("div");
      wrapper.innerHTML = templateEl.innerHTML.trim();
      const row = wrapper.firstElementChild;
      const titleEl = row.querySelector("[data-title]");
      const metaEl = row.querySelector("[data-meta]");
      if (titleEl) titleEl.textContent = item.title;
      if (metaEl) metaEl.textContent = `${item.section} · ${item.summary || ""}`;
      row.addEventListener("click", () => {
        window.location.href = item.url;
      });
      resultsEl.appendChild(row);
    });
    resultsEl.style.display = "block";
  };

  const filter = (query) => {
    const q = query.toLowerCase();
    return data.filter((item) => {
      return (
        item.title.toLowerCase().includes(q) ||
        (item.summary && item.summary.toLowerCase().includes(q)) ||
        (item.section && item.section.toLowerCase().includes(q))
      );
    });
  };

  input.addEventListener("input", (event) => {
    const value = event.target.value.trim();
    if (value.length < 2) {
      resultsEl.style.display = "none";
      resultsEl.innerHTML = "";
      return;
    }
    render(filter(value));
  });

  document.addEventListener("click", (event) => {
    if (!resultsEl.contains(event.target) && event.target !== input) {
      resultsEl.style.display = "none";
    }
  });
})();
