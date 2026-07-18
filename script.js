/* ============================================================
   Sam & Ivan The Chimney Guys — script.js
   Scroll reveal, animated counters, sticky header, mobile menu.
   ============================================================ */
(function () {
  "use strict";

  /* ---------- Always open at the top ---------- */
  // Mobile Safari can apply its native "scroll to #hash" behavior late, after
  // layout settles, which wins over a single early scrollTo(0,0). Reassert it
  // at every stage of the load lifecycle so it always wins, and drop the hash
  // so a tab that iOS reloads later (after being suspended) opens clean.
  if ("scrollRestoration" in history) history.scrollRestoration = "manual";
  if (location.hash) history.replaceState(null, "", location.pathname + location.search);

  function forceTop() { window.scrollTo(0, 0); }
  forceTop();
  document.addEventListener("DOMContentLoaded", forceTop);
  window.addEventListener("load", forceTop);
  window.addEventListener("pageshow", forceTop);
  setTimeout(forceTop, 0);
  setTimeout(forceTop, 300);

  /* ---------- Sticky header shadow ---------- */
  const header = document.getElementById("header");
  const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 10);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Mobile menu ---------- */
  const hamburger = document.getElementById("hamburger");
  const mobileMenu = document.getElementById("mobileMenu");
  const toggleMenu = (open) => {
    hamburger.classList.toggle("open", open);
    mobileMenu.classList.toggle("open", open);
    hamburger.setAttribute("aria-expanded", String(open));
    document.body.style.overflow = open ? "hidden" : "";
  };
  hamburger.addEventListener("click", () =>
    toggleMenu(!mobileMenu.classList.contains("open"))
  );
  mobileMenu.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => toggleMenu(false))
  );

  /* ---------- Scroll reveal + staggering ---------- */
  const reveals = document.querySelectorAll(".reveal");
  // Stagger siblings inside grid groups for a cascading effect.
  document
    .querySelectorAll(".cards, .why__grid, .reviews__grid, .pills, .gallery__grid")
    .forEach((group) => {
      group.querySelectorAll(".reveal").forEach((el, i) => {
        el.style.setProperty("--d", i * 0.08 + "s");
      });
    });

  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -60px 0px" }
    );
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("in"));
  }

  /* ---------- Animated counters ---------- */
  const counters = document.querySelectorAll(".stat__num");
  const runCounter = (el) => {
    const target = +el.dataset.count;
    const dur = 1600;
    const start = performance.now();
    const step = (now) => {
      const p = Math.min((now - start) / dur, 1);
      // easeOutExpo
      const eased = p === 1 ? 1 : 1 - Math.pow(2, -10 * p);
      el.textContent = Math.round(target * eased).toLocaleString();
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if ("IntersectionObserver" in window) {
    const co = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            runCounter(entry.target);
            co.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.6 }
    );
    counters.forEach((el) => co.observe(el));
  } else {
    counters.forEach((el) => (el.textContent = el.dataset.count));
  }

  /* ---------- Subtle hero parallax ---------- */
  const heroVisual = document.querySelector(".hero__visual");
  if (heroVisual && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    window.addEventListener(
      "scroll",
      () => {
        const y = window.scrollY;
        if (y < 900) heroVisual.style.transform = `translateY(${y * 0.06}px)`;
      },
      { passive: true }
    );
  }

  /* ---------- Contact form (demo handler) ---------- */
  const form = document.getElementById("estimateForm");
  const note = document.getElementById("formNote");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      note.hidden = false;
      note.scrollIntoView({ behavior: "smooth", block: "center" });
      form.reset();
      // NOTE: Wire this up to email/Formspree/your CRM when ready.
    });
  }

  /* ---------- Footer year ---------- */
  const yr = document.getElementById("year");
  if (yr) yr.textContent = new Date().getFullYear();
})();
