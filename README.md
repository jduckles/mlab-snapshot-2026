# M-Lab Snapshot 2026

**Live page:** <https://jduckles.github.io/mlab-snapshot-2026/>

An independent synthesis of what 15+ years of M-Lab's open Internet measurement record has been used to show — and where else the same record can go.

I compiled this from 61 posts in M-Lab's blog archive, 2013–2026. It is not an official M-Lab publication. I am offering it back to the M-Lab community for reuse, correction, and expansion.

## What is here

- `index.html` — generated at build time; the GitHub Pages page with the linked timeline and full annotated inventory.
- [`measurement-retrospective.svg`](measurement-retrospective.svg) — the standalone timeline. Each milestone links to its source post.
- [`measurement-data-inventory.md`](measurement-data-inventory.md) — the annotated inventory, with 81 inline citations to 61 posts.
- `social-card.png` — 1200×630 Open Graph and Twitter card image.
- `template.html`, `styles.css`, `build.py` — the build that turns the Markdown and SVG into the page.

## The argument

A speed test answers a narrow question. The record it leaves behind answers many others: interconnection disputes, disaster resilience, pandemic demand, broadband policy, throttling, routing, protocol design, and the measurement system itself.

The inventory is organized around that reuse. The cases are real, the numbers are sourced, and the limits are stated. The conclusion is deliberately modest: latent value is the return on keeping the raw record, publishing the methods, and being able to rerun the analysis in public.

## Build

Requires [Pandoc](https://pandoc.org/).

```sh
python3 build.py
open index.html
```

This regenerates `index.html` from `measurement-data-inventory.md`, `measurement-retrospective.svg`, and `template.html`.

GitHub Actions rebuilds and deploys the page whenever `measurement-data-inventory.md`, the SVG, the template, the stylesheet, the social card, or the build script changes on `main`. The generated `index.html` is not tracked.

## Links

All citations use the published M-Lab slug, without the ISO date prefix. For example:

```text
https://measurementlab.net/blog/hermes/
```

Every citation in the inventory was checked and resolves.

## License and provenance

The snapshot text and SVG in this repository are licensed under [CC BY 4.0](LICENSE). The linked M-Lab posts, measurements, and data remain M-Lab's work and are subject to M-Lab's own terms. Attribution should name M-Lab as the source of the underlying measurements and link to the original posts.

If you reuse or adapt this snapshot, a link back to the live page or repository is appreciated.
