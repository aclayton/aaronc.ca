# aaronc.ca

A hand-written static site. **No build step, no framework, no external requests** — the HTML
is served as it is written, and every asset is same-origin.

## Deploy

Netlify serves this directory whole (`publish = "."` in `netlify.toml`). Push to the default
branch, or drag the folder into the Netlify UI.

`netlify.toml` sets `command` to a deliberate no-op. This repo previously held a Vue 2 app
whose build command was `npm run build` → `dist`; if the Netlify UI still carries that setting
it will run, fail (there is no `package.json` any more), and block the deploy. `netlify.toml`
takes precedence over the UI, which is why the no-op lives there.

## Layout

| Path | What it is |
|---|---|
| `index.html` | Home |
| `work/bug-investigation/` | Case study |
| `work/finance-automation/` | Case study |
| `work/voice-knowledge/` | Case study |
| `404.html` | Not-found page — also the target of every 404 guard in `netlify.toml` |
| `style.css` | All styling; the design tokens live in `:root` |
| `accent.js` | Sets the day's accent hue. Progressive — the page is complete without it |
| `ground.js` | Hero ground parallax. Progressive |
| `fonts/` | IBM Plex Sans + Mono, self-hosted, four files, ~91 KB |
| `print/` | Printable flyer |
| `llms.txt` | Machine-readable summary for AI agents |
| `netlify.toml` | Headers, cache policy, and the 404 guards |

## Conventions

- **No external requests.** Fonts are self-hosted; no CDN, no analytics, no third party of any
  kind. The CSP in `netlify.toml` enforces it: `default-src 'self'`.
- **Illustrations are inline SVG, never images.** They inherit `--fg`, `--rule` and
  `--accent-fill`, so they follow the reader's theme and the day's hue for free, scale without
  loss, and add no requests.
- **Every SVG `<text>` is measured against its viewBox.** A caption past the edge is silently
  clipped — no scrollbar, no warning. Rotated text with no `text-anchor` runs past the bottom
  of the frame; this has bitten twice.
- **`publish = "."` means anything in this directory is served.** Anything that must not be
  public gets a guard in `netlify.toml` *and* stays out of this directory entirely — a redirect
  is a net, not a lock.
- **A `/404.html` must exist.** Every guard points at it; without it they fall back to
  Netlify's default page.

## Design

The layout reads from one proportional sequence — spacing `8 · 13 · 21 · 34 · 55 · 89`, type
`1 · √φ · φ · φ² · φ³`, body leading φ and headings √φ. The measure is derived from the
container rather than a `ch` count, so it stays exact when the font changes.

The ground is a cool neutral carrying a single accent hue. The hue changes daily; saturation
and both lightnesses are pinned per hue, so every day holds the same contrast ratio and no day
reads as weaker than another.
