# Sam & Ivan The Chimney Guys — Website

A modern, rounded, fully-responsive one-page site in the brand's red / white / black colors.

## Files
- `index.html` — home page content & structure
- `styles.css` — all styling, animations, hover effects, responsive layout (shared by every page)
- `script.js` — scroll reveals, animated counters, sticky header, mobile menu, form handler
- `services/*.html` — one landing page per service (generated, see below)
- `build_services.py` — generator for the service pages

## Service landing pages
Each dropdown item (8 chimney services + 5 related services) has its own page under
`services/`, all sharing the same header, footer, nav, and styling. They're linked from the
nav dropdowns and the homepage service cards/pills.

**To edit a service page's content** (heading, intro, benefits, warning signs, steps), open
`build_services.py`, edit that service's entry in the `SERVICES` dict, then regenerate:

```bash
python3 build_services.py
```

This rewrites every file in `services/` from the data, so all pages stay perfectly
consistent. Each hero has a "Photo coming soon" placeholder you can fill in the same way as
the others (add a `style="background-image:url('../images/yourphoto.jpg'); ..."` on the
`.service-hero__img` element).

## Run / preview locally
Open `index.html` through a local server (the CSS/JS won't load from a bare `file://` on some browsers):

```bash
cd sam-ivan-chimney
python3 -m http.server 4599
# then visit http://localhost:4599
```

## Adding your photos (the placeholders)
Every gray diagonal-striped box is a **photo placeholder**. To drop in a real photo, add an
inline background image to that element — the placeholder label disappears automatically.

1. Put your image in the `images/` folder (e.g. `images/hero.jpg`).
2. In `index.html`, find the placeholder — each has a `data-photo="..."` label describing it —
   and add a `style` with the image:

```html
<!-- before -->
<div class="hero__card image-frame" data-photo="Hero photo — crew on the roof / featured job">

<!-- after -->
<div class="hero__card image-frame" data-photo="Hero photo"
     style="background-image:url('images/hero.jpg'); background-size:cover; background-position:center;">
```

Placeholders to fill: hero, About (2), Gallery (6), and the Service-Area map.

## Wiring up the contact form
The form currently shows a success message but doesn't send anywhere yet.
To receive submissions, point it at a service like [Formspree](https://formspree.io):

- In `index.html`, change `<form ... id="estimateForm">` to
  `<form action="https://formspree.io/f/YOUR_ID" method="POST" id="estimateForm">`
- In `script.js`, remove the `e.preventDefault()` line so the form actually posts (or keep it
  and use Formspree's AJAX endpoint).

## Editable content
- **Phone / email / Instagram** — search for `978-320-7778`, `inschimneyguys@gmail.com`,
  `sam_n_ivan_chimneyguys` and update if needed.
- **Reviews** — the 3 testimonials are placeholders; swap in real Google/Facebook quotes.
- **Service-area towns** — edit the tag list in the `#areas` section.
- **Brand colors** — change the `--red`, `--ink`, etc. variables at the top of `styles.css`.
