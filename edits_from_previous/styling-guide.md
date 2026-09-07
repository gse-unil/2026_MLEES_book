# Styling guide, derived from Part I (1.1 and 1.2)

Working notes, not published content. Extracted directly from
[01-environment-and-data-types.ipynb](../part-I/01-environment-and-data-types.ipynb) and
[02-data-structures-and-control-flow.ipynb](../part-I/02-data-structures-and-control-flow.ipynb),
plus their paired `-exercises.ipynb` files. Purpose: a single reference for applying Part I's
visual system to ported material, starting with Part II chapter 2.

## Numbering

- **Subchapter title (H1):** `# {chapter}.{subchapter}) {Title}` — e.g. `# 1.1) Variables, Data
  Types, Operators and File I/O`, `# 1.2) Data Structures and Control Flow`. The `)` after the
  number, not a `.`.
- **Section headers (H2):** `## {chapter}.{subchapter}.{section} {Title}` — e.g.
  `## 1.1.1 Variables and the core scalar types`, `## 1.2.3 Functions`. Sections number
  sequentially through the notebook; sub-sections under a numbered H2 use plain `### Title` with
  no number (e.g. `### Lists`, `### Tuples`, `### Dictionaries` all sit under `## 1.2.1 Data
  Structures` unnumbered).
- **Fixed-role headers carry no number:** the AI-critique header, `## Summary` (1.1 only),
  `## Resources`. These are structural landmarks that repeat by name across every subchapter, not
  content sections, so they stay out of the numbering sequence.
- **Exercises notebooks are not numbered** — `# Exercises`, then `## Exercise 1: {name}`,
  `## Exercise 2: {name}`, …, sequential and un-prefixed by chapter number.

## Page structure (lecture notebook)

Fixed order, confirmed identical in both 1.1 and 1.2:

1. **H1 title** (numbered, see above).
2. **Intro paragraph**, 2–4 sentences: what the notebook covers, then the one running example
   carried through it (e.g. 1.1's alpine temperature readings, 1.2's station catalogue).
3. Optional **`{admonition} Before you start`**, `:class: note` — only where a real prerequisite
   exists (1.1 points at the appendix setup instructions). Not present in 1.2, so it is
   conditional, not a fixed slot.
4. Optional **`{figure}`** — a cover image, credited in the caption. Decorative, not load-bearing;
   skip it rather than force one.
5. **Learning objectives** — `{admonition} **Learning objectives**`, `:class: tip`, a bullet list
   of what the reader will be able to do. Always present, always this class.
6. **Numbered content sections** (`## {c}.{s}.{n} Title`), each free to use whichever boxes below
   fit the content. `### ` subsections group related material inside one numbered section without
   taking their own number.
7. **`## *When generated code lies: {specific bug}*`** — italicised, chapter-specific subtitle
   after the colon. Shows the bug running with a wrong answer, then a
   **`{admonition} **Diagnosis: {short name}**`**, `:class: warning`, explaining the mechanism and
   the fix, then the corrected code.
8. **Takeaways** — `{admonition} **Takeaways**`, `:class: danger`, bullets restating the
   subchapter's key rules; going-deeper points inside it are prefixed `*(Going deeper)*` /
   `*(going deeper)*` rather than pulled into their own bullet style (spelling of "going deeper"
   is inconsistent between 1.1 and 1.2 — capital G in 1.1, lowercase in 1.2).
9. Optional **`## Summary`** table (`Concept | Rule to remember`) — present in 1.1, absent in 1.2.
   Not a fixed slot; use when a compact recap table adds something the takeaways box doesn't.
10. **`## Resources`** — a short bullet list of external links, each `[Title](url) — one-line
    description of what it's for and why it's the natural next step`.

## Page structure (exercises notebook)

Looser, and — as actually written in 1.1 and 1.2, not as CLAUDE.md's abstract description of the
convention — simpler than the lecture:

1. **`# Exercises`** title, no intro note box in either 1.1 or 1.2 (CLAUDE.md describes one; the
   files on disk don't have it — flagging the mismatch rather than silently picking one).
2. **`## Exercise {n}: {short name}`**, prompt paragraph(s), optionally a fenced code block or
   table if the exercise needs given data.
3. **Empty code cell, `# Your solution here`** immediately below. No inline solution dropdown in
   either file — separate `-solutions.ipynb` files exist on disk but are commented out of
   `myst.yml`'s `toc`, so they aren't currently wired into the built book.
4. The long, real-dataset exercise at the end (1.1's Exercise 8) is flagged as multi-step
   (`**Step 1.** … **Step 2.** …`), pulls its data through `pooch.retrieve` with a `known_hash`,
   and ends `### To be continued (see next Exercises) ...` rather than being fully self-contained
   — a forward pointer to the next subchapter's exercises, not a dead end.

## Connections between pages

- Every subchapter is a **pair**: `{n}-{slug}.ipynb` (lecture) +
  `{n}-{slug}-exercises.ipynb` (exercises), nested as `children:` under the lecture file in
  `myst.yml`'s `toc`. A `-solutions.ipynb` sibling exists per pair but is commented out.
- Cross-references between subchapters are prose, not links: 1.2 tells the reader "the same
  slicing syntax will return on lists in the next subchapter and on arrays in 1.3" and "this is
  the idea behind the NaN-aware operations you will meet in the next subchapter" — forward
  pointers by name, no hyperlink machinery.
- The **AI-critique bugs deliberately echo each other** across subchapters (documented already in
  the project CLAUDE.md: 1.2's mutable default argument and 1.7's shared class attribute are the
  same mechanism twice). 1.2's own going-deeper box on pure/impure functions explicitly primes the
  reader for this: "Keep this in mind while reading the generated-code bug at the end of this
  subchapter — it is the same mechanism."
- The appendix is referenced, not duplicated: 1.1's "Before you start" box links to
  `../appendix/appendix.md` rather than re-explaining setup.

## Admonition syntax

MyST fence, three lines minimum:

```markdown
:::{admonition} {Title}
:class: {role}
{body}
:::
```

Dropdown variant adds `dropdown` to the class list (`:class: seealso dropdown`,
`:class: note dropdown`) — content is collapsed behind a click.

## Admonition palette (from CLAUDE.md, cross-checked against 1.1/1.2)

| Role | Class | Title style seen in 1.1/1.2 |
|---|---|---|
| Learning objectives | `tip` | `**Learning objectives**` |
| Takeaways | `danger` | `**Takeaways**` |
| Computational-thinking fundamental (max one per subchapter) | `important` | `**Computational-thinking fundamental: {specific insight}**` |
| Going deeper (optional depth) | `seealso dropdown` | `**Going deeper: {topic}**` (or, once, plain `Going deeper: docstrings` without bold) |
| Code pitfalls, AI-critique diagnoses | `warning` | `**Diagnosis: {short name}**`, `**Common mistake**: {rule}`, `Rules for naming a variable:` |
| General asides, definitions | `note` | `Before you start`, `**`{range()}` method**`, `**The key fact about file input**` |
| Solutions | `note dropdown` | not yet used in 1.1/1.2 exercises (see above) |

Observed convention: the admonition **title itself is usually bold** (`**Title**`), even though
the class already carries the visual weight — inconsistently applied (some titles, like `Before
you start` and the `range()` box, are not bold). Treat bold-by-default as the norm, not a hard
rule.

## What this means for Part II chapter 2

Chapter 2 keeps the reference's own structure (tutorial + several standalone exercise notebooks,
not the lecture/exercises pairing above — see CLAUDE.md's "Current state"). It does not have
Part I's fixed slots (no AI-critique, no Takeaways, no Summary table) and shouldn't grow them —
that would be rewriting, not styling. What it borrows from this guide is narrower: **the
admonition palette itself**, applied to structural elements chapter 2 already has that map
cleanly onto a role above — starting with the "Learning Objectives" list in
2.1-classification-and-regression.ipynb, which becomes a `tip` box exactly as in 1.1/1.2.
