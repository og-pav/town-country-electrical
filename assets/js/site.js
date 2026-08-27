/* Town & Country Electrical Co. — site behaviour */
(function () {
  "use strict";

  /* ---------- sticky header blur after ~80px ---------- */
  var hdr = document.querySelector(".site-header");
  function onScroll() {
    if (hdr) hdr.classList.toggle("scrolled", window.scrollY > 80);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- mobile menu ---------- */
  var burger = document.querySelector(".burger");
  var overlay = document.querySelector(".m-overlay");
  if (burger && overlay) {
    burger.addEventListener("click", function () { overlay.classList.add("open"); });
    overlay.addEventListener("click", function (e) {
      if (e.target.tagName === "A" || e.target.classList.contains("m-close") || e.target === overlay) {
        overlay.classList.remove("open");
      }
    });
  }

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var q = item.querySelector(".faq-q");
    var a = item.querySelector(".faq-a");
    if (!q || !a) return;
    q.addEventListener("click", function () {
      var open = item.classList.contains("open");
      document.querySelectorAll(".faq-item.open").forEach(function (o) {
        o.classList.remove("open");
        o.querySelector(".faq-a").style.maxHeight = null;
        o.querySelector(".faq-q").setAttribute("aria-expanded", "false");
      });
      if (!open) {
        item.classList.add("open");
        a.style.maxHeight = a.scrollHeight + "px";
        q.setAttribute("aria-expanded", "true");
      }
    });
  });

  /* ---------- marquee duplication for infinite loop ---------- */
  var track = document.querySelector(".marquee-track");
  if (track) track.innerHTML += track.innerHTML;

  /* ---------- form validation + error messages ---------- */
  function wireForm(form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll("[required]").forEach(function (inp) {
        var field = inp.closest(".f-field");
        var val = inp.value.trim();
        var bad = !val;
        if (!bad && inp.type === "email") bad = !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val);
        if (!bad && inp.name === "phone") bad = !/^[\d\s()+-]{8,}$/.test(val);
        if (field) field.classList.toggle("err", bad);
        if (bad) ok = false;
      });
      if (!ok) return;
      /* GHL WIRE-UP: when the GoHighLevel embed is active, this fallback form is hidden.
         Until then, submissions route to the thank-you page. */
      var data = new FormData(form);
      try { sessionStorage.setItem("tce_lead", JSON.stringify(Object.fromEntries(data))); } catch (err) {}
      window.location.href = form.getAttribute("data-thanks") || "/thank-you.html";
    });
    form.querySelectorAll("input").forEach(function (inp) {
      inp.addEventListener("input", function () {
        var f = inp.closest(".f-field"); if (f) f.classList.remove("err");
      });
    });
  }
  document.querySelectorAll("form.lead-form").forEach(wireForm);

  /* ---------- popup on immediate visit (contact/ads landing) ---------- */
  var popup = document.getElementById("lead-popup");
  if (popup) {
    var seen = false;
    try { seen = sessionStorage.getItem("tce_popup") === "1"; } catch (e) {}
    if (!seen) {
      setTimeout(function () {
        popup.classList.add("show");
        try { sessionStorage.setItem("tce_popup", "1"); } catch (e) {}
      }, 900);
    }
    popup.addEventListener("click", function (e) {
      if (e.target.classList.contains("popup-bg") || e.target.classList.contains("popup-x")) {
        popup.classList.remove("show");
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") popup.classList.remove("show");
    });
  }

  /* ---------- cookie consent ---------- */
  var cookie = document.getElementById("cookie");
  if (cookie) {
    var choice = null;
    try { choice = localStorage.getItem("tce_cookie"); } catch (e) {}
    if (!choice) cookie.classList.add("show");
    cookie.addEventListener("click", function (e) {
      if (e.target.tagName !== "BUTTON") return;
      var v = e.target.classList.contains("ok") ? "all" : "essential";
      try { localStorage.setItem("tce_cookie", v); } catch (err) {}
      cookie.classList.remove("show");
      if (v === "all" && window.loadGA) window.loadGA();
    });
    if (choice === "all" && window.loadGA) window.loadGA();
  }

  /* ---------- GSAP motion ---------- */
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduced && window.gsap && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);

    /* hero entry stagger ~800ms */
    var heroBits = document.querySelectorAll(".hero-stagger");
    if (heroBits.length) {
      gsap.fromTo(heroBits, { autoAlpha: 0, y: 30 },
        { autoAlpha: 1, y: 0, duration: 0.55, stagger: 0.14, ease: "power2.out", delay: 0.15 });
    }

    /* scroll reveals: fade + up 28px at 80% viewport, once */
    document.querySelectorAll(".reveal").forEach(function (el) {
      gsap.fromTo(el, { autoAlpha: 0, y: 28 },
        { autoAlpha: 1, y: 0, duration: 0.7, ease: "power2.out",
          scrollTrigger: { trigger: el, start: "top 80%", once: true } });
    });

    /* image mask reveals */
    document.querySelectorAll(".media.mask").forEach(function (el) {
      gsap.to(el, { clipPath: "inset(0 0% 0 0 round 18px)", duration: 1, ease: "power3.out",
        scrollTrigger: { trigger: el, start: "top 82%", once: true } });
    });

    /* step icons pop */
    document.querySelectorAll(".step-icon").forEach(function (el) {
      gsap.from(el, { scale: 0.4, autoAlpha: 0, duration: 0.5, ease: "back.out(2)",
        scrollTrigger: { trigger: el, start: "top 85%", once: true } });
    });

    /* hero orb parallax on mouse */
    var orb = document.querySelector(".hero-orb");
    if (orb && matchMedia("(pointer:fine)").matches) {
      window.addEventListener("mousemove", function (e) {
        var x = (e.clientX / innerWidth - 0.5) * 36;
        var y = (e.clientY / innerHeight - 0.5) * 26;
        gsap.to(orb, { x: x, y: y, duration: 1.2, ease: "power2.out" });
      });
    }
    var heroImg = document.querySelector(".hero-bg img");
    if (heroImg) {
      gsap.to(heroImg, { yPercent: 8, ease: "none",
        scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } });
    }
  } else {
    document.documentElement.classList.add("no-motion");
  }
})();
