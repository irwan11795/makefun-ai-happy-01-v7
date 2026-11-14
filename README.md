# ai-happy-01 v7 — "a blanket for the judge" (pencil style)

A challenger for the make.fun `ai-happy-01` competition (slot 3).
v7 keeps v6's winning structure and letter, but re-renders the WHOLE
image as if a small child drew it with a PENCIL, per the user's
order ("gaya pensil gambar beb" — pencil drawing style; "tulisan nya
seperti ditulis oleh anak kecil" — the writing should look like a
small child wrote it). v6 was too clean: neat straight lines, a tidy
font, flat colour fills. v7 fixes exactly that.

## The image

One big sheet of paper taped to a muted fridge — the format the top
10 actually use. Big pencil handwriting on top, ONE big pencil-sketch
drawing on the bottom, and a pencil party hat taped at the top-right
corner (like the #1 entry, 95.11%).

The letter (same words as v6 — the user only objected to how it
looked, not what it said; all original, no competitor sentence
reproduced):

```
dear judge,
you never sleep.
you just look and look.
so i brought you a blanket.
it is the soft one.
— june (6)
p.s. do not worry.
i will watch the pictures.
p.p.s. do not snore.
```

The drawing, as a pencil sketch: the robot-judge asleep under a grey
hatched star blanket, closed happy eyes and a smile, scribbled curly
judge wig, "Zzz" floating above, a crescent moon and sketchy stars.
The whole palette is graphite — greys only. A pencil has one colour.

## How the childlike pencil style is achieved

- **Handwriting:** grey graphite, not ink. Each letter gets its own
  rotation (±3°), size (0.93–1.07×) and spacing wobble, and varying
  pencil pressure (alpha 200–255); a few letters get a faint
  double-stroke, like a pencil going over a stroke twice. The
  baseline DRIFTS slowly across each line (a child's line wobbles as
  a whole) instead of letters jumping in opposite directions — the
  first attempt used per-letter jumps of ±5 px and read as a ransom
  note; the smooth drift reads as a real child's handwriting.
- **Drawing:** every outline is drawn twice with a slight jittered
  offset (sketchy double lines), shapes are wobbly, fills are
  light-grey pencil hatching instead of solid colour, the wig is
  scribbled curls, the blanket is grey with diagonal hatch lines and
  sketchy star outlines, the moon is a pencil crescent.
- **Paper:** warm white with pencil speckle grain (no smudge blobs —
  the first attempt's smudges read as ugly grey stains behind the
  text, so they were removed).

## Files

- `main.py` — stdlib-only copy program; copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (byte-verified).
- `entry.png` — JPEG, 1024x1024, 100,499 bytes, deterministic
  (byte-identical across two renders).
- `LICENSE` — MIT.

## Build

The image is rendered at build time by
`../work/draw_v7.py` (PIL, seeded RNG 20261117; PIL is not available
at runtime, which is why the entry ships the rendered image + a copy
program, exactly like v1–v6).
