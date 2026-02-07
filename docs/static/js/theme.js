(function () {
  const root = document.documentElement;
  const btn = document.getElementById("theme-toggle");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const saved = window.localStorage.getItem("theme");
  const initial = saved || (prefersDark ? "dark" : "light");

  const apply = (mode) => {
    root.setAttribute("data-theme", mode);
    window.localStorage.setItem("theme", mode);
  };

  apply(initial);

  if (btn) {
    btn.addEventListener("click", () => {
      const current = root.getAttribute("data-theme") === "dark" ? "dark" : "light";
      apply(current === "dark" ? "light" : "dark");
    });
  }

  const nav = document.querySelector(".top-nav");
  if (nav) {
    const handleScroll = () => {
      if (window.scrollY > 10) {
        nav.classList.add("nav-scrolled");
      } else {
        nav.classList.remove("nav-scrolled");
      }
    };
    handleScroll();
    document.addEventListener("scroll", handleScroll, { passive: true });
  }
})();
