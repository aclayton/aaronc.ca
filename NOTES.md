# aaronc.ca — new site (v1 draft, 2026-11-06)

Hand-written static site. **No build step, no JavaScript, no dependencies.** Three files do
the work: `index.html`, `style.css`, `favicon.svg`.

## Why this shape

The old site was a Vue 2.5.17 SPA (Aug 2018 — Vue 2 reached end of life Dec 2023) that
presented Aaron as a *"Front-end Developer"* with a Vue/Vuex/Node/MongoDB stack list. This
one is built around the actual positioning:

> **"I make complex systems people actually use, then take the manual work out of them."**

Three deliberate consequences:

1. **No technology list in the pillars.** Technology dates; what it *does for the reader*
   doesn't. The stack appears at the bottom of each case study as supporting detail.
2. **Real projects, not a skills grid.** The three case studies are things Aaron actually
   built and can talk about under questioning.
3. **The site is the first piece of evidence.** A UX-minded person's own site should respect
   `prefers-color-scheme` and `prefers-reduced-motion`, be keyboard-navigable, work with
   JavaScript disabled (there is none), and not shift layout on load.

## Colour

A cool neutral ground with a single accent hue. The hue is the only thing that varies.

| | Light | Dark | Contrast |
|---|---|---|---|
| page | `#f7f6fa` | `#0b0910` | — |
| band | `#eeebf6` | `#141120` | 24 / 33 channel delta — reads as a layer, not a seam |
| ink | `#191725` | `#e9e6f2` | 16.4:1 / 16.1:1 |
| muted | `#5e5a72` | `#9a94ae` | 6.1:1 / 6.8:1 |

The accent takes one hue per day. Saturation and both lightnesses are pinned per hue in
`style.css`, solved so that **every day carries identical contrast** — no day reads as weaker
than another. Light mode: fill is mid-dark carrying a white label (a solid button on paper).
Dark mode: fill is mid-light carrying a near-black label (a bright chip on near-black).

All 15 pairs verified at **5.05:1 or better**, in both themes.

**If you add or change a hue, re-solve all of them.** The point of the system is uniform weight;
hand-tuning one date breaks it.

`accent.js` sets `data-accent` on `<html>` from the weekday, reckoned sunrise to sunrise, so the
accent turns over at dawn rather than midnight. It is progressive enhancement — the page is
complete, correctly coloured, and passes AA without it, resting on the default hue.

The accent drifts in over a 2.4s transition rather than snapping.

**Note for whoever measures this:** a CSS transition means reading a computed colour returns the
*animating* value. Inject `transition: none` before measuring, or every hue will read identical.


## Hero

The mark **leads the page**, as on the old site — at `clamp(52px, 5.6vw, 68px)` tall, the same
step as the headline (φ³ × 16). At 32px in a header bar it was an illegible smudge, which is why
it moved out of the header and into the hero.

The header now carries the **name** instead. An abstract mark with no wordmark left first-time
visitors finishing the hero without knowing whose site it was.

**The mark is cropped flush.** Its artwork is 252×144 but the path starts at x=18, leaving an 18-unit
margin that pushed it ~8px inboard of the text gutter. The hero and footer use
`viewBox="18 0 216 144"` to crop that margin, so the mark sits exactly on the spine. Verified: 0px
offset from the headline.

Spacing is on a deliberate scale: mark→eyebrow 40px, eyebrow→h1 8px (the eyebrow belongs to the
headline), h1→lede 18px, lede→buttons 32px.

### The ground behind it

The hero sits on a ground built from the mark's own construction — two rings, centres one radius
apart, so their overlap reads as a soft lens — under a wash of the day's accent. Three things make
it work rather than becoming an artifact:

1. **It is full-bleed.** `inset-inline: calc(-50vw + 50%)` takes the layer to the viewport edge, so
   its dissolve happens in the page gutter. An earlier version faded at the container edge, where
   the ramp lined up with the text and read as a hard seam. `overflow-x: clip` on `<html>` absorbs
   the `100vw`/scrollbar difference without creating a scroll container.
2. **It is masked on both axes** (`mask-composite: intersect`), so nothing is guillotined. A 1px arc
   stopping dead draws more attention than any soft field does.
3. **The hairlines are drawn in ink** (`color-mix(in srgb, var(--fg) 22%, transparent)`), so they are
   light on dark and dark on light. Using `--rule` drew them in a *dark* colour in dark mode, where
   they very nearly vanished.

Wash is **10%** of the day's accent, hairlines **22%** ink. Both started lower (5% / 16%) and were
raised after a report that nothing was visible — a ground this faint moving 6px is undetectable, and
the fix was to make it present rather than to move it harder. Contrast survives to 15%+ (ink 13.4:1,
muted 5.0:1, ghost line 3.16:1), so both are taste dials, not legibility limits.

The vision review independently described the result as "a faint lens/vesica shape" — the geometry
reads as intended and the source names nothing.

### Motion

Two movements, and they run on **different CSS properties** so they add rather than overwrite:

- **`transform`** — a slow ambient drift (72s keyframe loop, `translate3d` 0 → −1.6%), so the ground
  breathes when nobody is moving anything.
- **`translate`** — `ground.js`, eased, from whichever input is moving. **Vertical only** — see below.
  - **scroll** — the ground lags behind the content by up to 40px across the hero, so it settles as
    the hero leaves. This is what a phone gets, and it's the interaction a touch device actually
    offers.
  - **pointer** — a ±18px drift against the pointer's *vertical* position.

**Vertical only, and that's a hard constraint.** The layer is full-bleed — it spans the viewport
exactly — so any horizontal displacement extends the scrollable area and produces a stray horizontal
scrollbar, and so does any `scale()` on it, because the box then grows in both axes. `overflow-x: clip`
on `<html>` does **not** absorb this reliably. Vertical movement costs nothing, because the page is
already taller than the viewport. If the pointer's X should matter again, the layer has to stop
spanning the viewport first, which costs the full-bleed edge. Verified: `canScrollX === 0` at 360 /
390 / 768 / 1024 / 1440 / 1600px and with the pointer at both extremes.

**Both are bound unconditionally, on purpose.** Switching between them on
`matchMedia('(pointer: coarse)')` looks tidier, but that branch cannot be exercised by the test
harness at all — and identical, *measured* behaviour on every device beats a clever branch that
ships unverified. On desktop you get both, which reads as continuity as the hero scrolls away.
`pointerType === 'touch'` is ignored, because on a touch device a drag would otherwise fight the
scroll.

The text never moves. Only the ground does. That's what makes it read as depth, not animation.

`ground.js` returns immediately under `prefers-reduced-motion` (a JS transform is invisible to the
CSS media query, so it must be checked in the script too), and listens for `change` so a mid-session
switch resets it. The rAF snaps to its target and returns without scheduling another frame, so there
is no background work.

**Device tilt is deliberately not implemented.** `DeviceOrientationEvent.requestPermission()` must be
called from a user gesture, and the API is blocked entirely outside a secure context — so it is
untestable on a plain-`http://` preview and would ship unverified. It belongs on the HTTPS deploy,
behind a tap-to-enable control, on phones only.

## Layout rule

**One container and one gutter for everything.** Every section, band, heading, card, header
and footer shares a single left edge — verified at every width from 320 to 1600.

The first version used `ch` for containers, which is relative to *each element's own
font-size*: an `h2` at 25px got a much wider `max-width` than a 16px paragraph, so the section
spine visibly broke. **Containers are `rem`; only text measures in `ch`.**

## Proportional system

Nothing on the page is an arbitrary number. Every measurement comes from one sequence:

```
spacing     8   13   21   34   55   89
type        1   1.272   1.618   2.618   4.236
leading     1.618  (body)     1.272  (headings)
measure     61.8ch
container   55.625rem
```

Verified in the browser:

| relationship | measured |
|---|---|
| spacing, adjacent steps | 1.6250 · 1.6154 · 1.6190 · 1.6176 · 1.6182 |
| type, adjacent steps | 1.6180 · 1.6180 · 1.6180 |
| body leading | 1.6180 |
| case-study label : content | 1.6181 |
| container : measure (890 : 550) | 1.6184 |
| hero mark : headline | 0.9998 |

Section rhythm, gutters, grid gaps, button padding, border radii, list indents and the
case-study grid all read from the same curve, so spacing and type are one system drawn at two
scales.

This is stated only as numbers. Do not annotate it.



## Files

| File | Purpose |
|---|---|
| `index.html` | The whole page: hero, pillars, three case studies, process, contact |
| `style.css` | Light/dark, fluid type, print styles, reduced-motion support |
| `logo.svg` | **The real mark**, from the old site's `public/img/ac.svg`. Fill changed to `currentColor` so one file serves light and dark |
| `favicon.svg` | The same mark, centred in a square for favicon use; inverts via `prefers-color-scheme` |
| `netlify.toml` | Zero-build publish config + security headers + CSP |
| `robots.txt`, `sitemap.xml` | Basic discoverability (was absent entirely) |
| `llms.txt` | Clean summary for AI agents — on-brand for applied-AI work |

## Before this goes live

**1. Fill in the `<!-- TODO -->` outcomes.** There are three, one per case study. They are
marked rather than filled because **inventing metrics on a portfolio is the fastest way to
lose a technical interview**, and only Aaron knows the real numbers. Suggested framing:

- Bug management: items processed per run, triage time before/after, % routed without a human
- Finance automation: how many statements/month, what the manual equivalent was, how long
  it's been running unattended
- Voice pipeline: notes captured since when, what capture used to cost in friction

**2. Create `og.png` (1200×630).** Referenced in the `<meta property="og:image">` tags but not
yet made. Without it, shared links render as a blank card — which is what happens today.
Direction: `logo.svg` on a plain background with the positioning line beside or beneath it.
Keep it in sync with the `<h1>`.

**3. This is a presence site, not a job hunt.** (Dude, 2026-11-06: *"Take out the available,
I have a job, want a presence."*) The hero eyebrow is location only, and the contact copy is
neutral — no availability, no "open to opportunities", no consulting pitch. Keep it that way.

> **Enforced 2026-11-18.** Dude flagged the page as *"too looking-for-work"* — and the contact
> section was breaking this rule: it read **"Get in touch / Happy to hear from people working on
> interesting problems"** with a form asking **"What are you working on?"**. That is an
> availability statement in soft clothes and a client-intake form, however neutral the hero was.
> Fixed: the hero's second button removed (one CTA left, pointing at the *work*), the heading is
> now **Contact**, the lede is the location fact only, and the form field is **Message**. The
> lesson: **a rule about vocabulary gets enforced and still fails at the level of layout.** The
> words were fine; the *shape* — claim, services, portfolio, method, invitation — is a services
> page. Watch the architecture, not only the adjectives.

**4. Check the finance case study for anything employer- or client-identifying.** It describes
the *pattern*, deliberately, not the data: no vendors, no amounts, no account numbers. Keep it
that way. `bill-tracker` was made private for the same reason.

> **No employer, anywhere on the site.** (Dude, 2026-11-18: *"Keep boost out of it."*) Asked whether
> the page should carry a "where I do it" section naming boostCX — **no.** Three reasons, recorded so
> it is not re-litigated: it is an **employment** frame, which is the sibling of the job-hunt frame
> this site exists to avoid; it would be the only **perishable** line on the page, and it would rot
> into something *wrong* rather than merely absent; and it is the one line with a **disclosure**
> question attached, on the surface that is publicly indexed and carries his name. The case studies
> already demonstrate the work as *pattern* with nobody named — the work speaks, the payer does not
> need to. If context is ever genuinely wanted, it is **one clause at most** ("Systems engineer,
> Niagara, Canada") — never a section, never a team, never a client.

## Deploying

```bash
# Netlify: drag this folder into the Netlify UI, or
netlify deploy --dir=. --prod
```

Netlify Forms needs the form present at deploy time — it is (`data-netlify="true"`), so
submissions will appear in the Netlify dashboard with **no backend at all**. That replaces the
dead Firebase Cloud Functions (`aaroncca-form-processor`, both returning 503) which were
silently swallowing every enquiry.

The visible `mailto:aaronc@protonmail.ch` fallback stays on purpose: a form is a single point
of failure, and it was the *only* failure mode on the old site.

## Deliberately not included yet

- **Writing / notes section** — the best long-term credibility and SEO, but it needs real
  posts, not placeholders. Add when there's something to say.
- **Astro or any framework** — unnecessary at this size. If the writing section grows past a
  handful of posts, port to Astro then; markdown content and a layout template is a small job.
- **A public "ask my portfolio" AI agent** — genuinely on-brand and the pattern already exists
  elsewhere, but it needs rate-limiting and cost control first. Phase two.

## Case-study pages

Each system has its own page. The home page carries a **synopsis** and links out; the detail page
carries the **write-up and the visuals**. Structure, so this stays maintainable:

| Page | URL | Visuals |
|---|---|---|
| Bug investigation | `/work/bug-investigation/` | pipeline diagram · trust-boundary diagram · a time-saved model grid (a table, not an SVG) |
| Finance automation | `/work/finance-automation/` | ingestion diagram · six-tier matcher diagram · two measured charts · **dashboard screenshot** |
| Voice-to-knowledge | `/work/voice-knowledge/` | pipeline diagram · the failed-design diagram · two-pipelines diagram |

**Editing this site — hard-won rules.**

- **The mark is inlined per page, and must never be "normalised" by shape.** Every page carries the
  brand mark as a literal `<path>` copied from `logo.svg`. A script that finds path elements whose
  `d` *looks like* the mark will match **every** path in the file, not just the mark: a real attempt
  at this replaced **41 connector lines across 7 figures** with copies of the logo. The mark is the
  only `<path>` on the page with **no `class` attribute** — if a script must identify it, key on that,
  and never on shape. Better: don't script it at all.
- **Never splice into a string using offsets from the pre-edit version.** Rebuilding those figures
  multiplied the damage: the second edit in each file used character offsets measured before the
  first edit, so the offsets drifted and **duplicated a whole figure block on every page**. The tell
  was an SVG count that had grown. Build edits with a cursor (`last = m.end()`), or write files whole.
- **This directory is not under version control and has no backup.** Both failures above would have
  been one `git checkout`. Until the site is a repo or on a snapshot schedule, every scripted edit to
  it is uninsured — and a mistake is permanent work, not a revert.
- **Measure rotated text against its viewBox.** A `<text>` with `transform="rotate(90 x y)"` and no
  `text-anchor` runs *downward* from its anchor point and will silently exit the bottom of the frame.
  This has now bitten twice on `/work/finance-automation/` — once by 51px, once by a third of a
  45-character caption. Check the screen rect of every text node against its figure's screen rect;
  a clip has no scrollbar and no error.

**Rules for these pages.**

1. **Synopsis on home, substance on the page.** If a paragraph could live on either, it belongs on
   the detail page — the home page's job is to make someone want to click, not to finish the argument.
2. **Illustrations are inline SVG, never images.** They inherit `--fg`, `--rule`, `--accent-fill`
   and the rest, so they follow the reader's theme and the daily hue for free, they scale without
   loss, and they add no requests. A PNG would have to be re-rendered twice and would be wrong in
   one of the two themes.
3. **Measure the SVG text against its viewBox.** Long captions silently clip — no scrollbar, no
   overflow warning, just a missing half-sentence. Check `x + bbox.width` against the viewBox width
   for every `<text>`; a caption 51px past the edge renders as a cut-off line and nothing else
   complains.
4. **Charts use the real system's data, and only what may be public.** The finance charts are counts
   and structure. **No amounts, no vendors, no account numbers.** A dashboard screenshot is where this
   gets dangerous, because the UI is full of figures.
5. **For a screenshot, use the app's own privacy control — then prove it worked.** The finance
   dashboard has a blur control, so its screenshot is taken with that on. But *do not trust a
   privacy feature to be complete*: before capturing, walk the DOM, regex every `$` figure in the
   rendered text nodes, and assert each one sits inside a blurred element. On the first run that
   check found **61 tagged spans and one untagged match**, and the untagged one was inside a
   `<script>` and never rendered — which is the only reason the screenshot shipped. The same run
   confirmed all four chart canvases carried a blur filter. A control that misses things is worse
   than no control, because it looks like it worked; the check is what makes the difference.
6. **Be honest about your own systems. Never publish someone else's weaknesses.** The voice page
   states its own open items — an endpoint on every interface, no shared secret — because that
   system is his and the disclosure is his to make. The bug system is **employer-owned**: saying
   "there is no CI and the tests are inadequate" on a personal site is a public engineering
   critique of a system he does not own, attached to his name, in a repository anyone can find and
   connect back. The same logic that keeps the employer's name off the site keeps its weaknesses
   off it too. State scope and design boundaries; leave the audit out.

## Checklist

- [ ] Fill in three case-study outcomes with true figures — **the TODO placeholders now live on the three detail pages**, one each
- [x] ~~Split work into detail pages, with synopses on home~~ — done 2026-11-18, nine inline SVG figures across the three, all text verified inside its viewBox
- [x] ~~Include the dashboard in the finance section~~ — done 2026-11-18. `work/finance-automation/dashboard.png`, captured from `:9000` with the dashboard's own blur engaged; safety verified by asserting every `$` figure in the rendered text sits inside a blurred span
- [ ] Create and commit `og.png`
- [x] ~~Confirm the hero availability line~~ — hero was already compliant; the **contact** copy was the violation. Fixed 2026-11-18.
- [ ] Re-read the page for *shape*, not vocabulary — the section order still reads as claim → services → portfolio → method → invitation
- [x] ~~Re-read the finance case study for identifying detail~~ — counts and structure only, verified 2026-11-18
- [x] ~~Put the site under version control~~ — done 2026-11-19. Repo is **`aclayton/aaronc.ca` (PUBLIC)** — the old Vue 2 app's own repo, now adopted: this directory is a git working copy on branch `static-rewrite`, and **PR #31** replaces the Vue app with the static site. Merging also clears **200 Dependabot alerts** on `master` (all from the retired `package-lock.json`).
  - `social/`, `vesica/` and this file (**renamed `NOTES.md`**) are gitignored and **not on the remote** — verified. A public repo has no equivalent of the `netlify.toml` guards, so those three stay out of the tree; the guards only cover the website.
  - Note the trap: `.gitignore` cannot exclude a path **already tracked** — the old repo had its own `README.md`, so the internal doc had to move to `NOTES.md` before a clean public `README.md` could take that path.
- [ ] Point `aaronc.ca` DNS at the new deploy (currently a Vue 2 SPA on Netlify, **and currently returning HTTP 500**)
  - Guards now: `/social/*`, `/vesica/*`, `/README.md`, `/NOTES.md`, `/netlify.toml`, `/.git/*`, `/.gitignore`
  - **Still unverified** — the local preview server does not read `netlify.toml` (`/social/` returns 200 locally). Prove them on a deploy preview before moving DNS.
  - `netlify.toml` now sets `command` to a no-op; the old build was `npm run build` → `dist` and would fail with `package.json` gone. `netlify.toml` overrides the Netlify UI.
- [ ] Update the GitHub bio to match the new positioning
