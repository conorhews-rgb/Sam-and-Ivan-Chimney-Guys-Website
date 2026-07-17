# Sam & Ivan The Chimney Guys — Website

A modern, rounded, fully-responsive one-page site in the brand's red / white / black colors.

## Files
- `index.html` — page content & structure
- `styles.css` — all styling, animations, hover effects, responsive layout
- `script.js` — scroll reveals, animated counters, sticky header, mobile menu, form handler

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
