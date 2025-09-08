---

<!-- README.md -->

### Bella & Piper: Classical Singing Curriculum (Ages 3 and 5)

This folder contains a comprehensive, pick-up-where-you-left-off curriculum designed for one dedicated session per child per week. It follows a Classical approach (Grammar → Logic → Rhetoric), integrates hymn singing on Sundays if desired, and includes sheet music and ready-to-run parent scripts.

### Quick Start
- Open `Curriculum_Overview.md` to understand the approach and goals.
- Check `Scope_and_Sequence.md` (now a progression map) to see the ordered skill path with expected age ranges.
- Use `Weekly_Sessions.md` (now progression checkpoints) for step-by-step activities you can do in any cadence.
- Open the referenced score in `sheet_music/` for the song/exercise.
- Mark progress in `Progress_Tracker.md` by level and checkpoint.

### One-day-a-week friendly
- Each checkpoint is self-contained. Do one or several when you have time.
- If you pause, resume at the last incomplete checkpoint; no rework needed.

### Classical Approach (at a glance)
- Grammar (Ages ~3–6): Memorize songs/solfège, posture, breath, steady beat, clear diction.
- Logic (Ages ~6–9): Read notes/rhythms, recognize intervals, sing simple harmony/rounds.
- Rhetoric (Ages ~9+): Expressive storytelling, style choices, small recitals.

### Folder/File Index
- `Curriculum_Overview.md` — Philosophy, goals, materials, how-to-run sessions.
- `Scope_and_Sequence.md` — Progression map of skills, songs, and scores (with expected age ranges).
- `Weekly_Sessions.md` — Progression checkpoints with Age 3 adaptations and Age 5 extensions.
- `Parent_Scripts_Age3.md` — "Say this" scripts and checklists for Bella (3yo).
- `Parent_Scripts_Age5.md` — Scripts and checklists for Piper (5yo).
- `Progress_Tracker.md` — Track levels and checkpoints, not weeks.
- `sheet_music/` — LilyPond scores for warmups and core songs. See `sheet_music/README.md` for how to export PDFs.
- `build_curriculum.py` — Compile all Markdown into one file and optional PDF.
- `MANIFEST.json` — Optional custom order for compilation.

### Tools (optional)
- LilyPond (to export PDFs from `.ly` files). Install instructions in `sheet_music/README.md`.

### Related
- Existing general plan: `Comprehensive Singing Lesson Plan for Kids (4).markdown`. The new files here specialize that plan for the 3yo/5yo tracks and a once-per-week schedule.

---

<!-- Curriculum_Overview.md -->

### Curriculum Overview (Classical Approach)

This curriculum is designed for Bella (3) and Piper (5) with one lesson per child per week. Lessons are self-contained and progressive, so you can pause and resume anytime. The approach follows the Classical trivium:

- Grammar (3–6): memorize songs and patterns, form healthy habits (posture, breath, diction), internalize beat and pitch.
- Logic (6–9): connect facts, read notation and rhythms, recognize intervals, sing simple harmony/rounds.
- Rhetoric (9+): communicate meaning, shape phrases, make stylistic choices, perform for an audience.

### Goals by Age Track
- Age 3 (Bella): joyful vocal exploration, simple solfège (do–so), steady beat, clear words, 1–2 short songs by memory.
- Age 5 (Piper): accurate pitch center, 5-note scale patterns (do–so), basic rhythm reading (quarter/half rests), first rounds/harmony with parent, 2–3 songs by memory.

### Session Structure (30–40 minutes)
1) Welcome & posture (2–3 min)
2) Breath + light warmups (5–7 min)
3) Technique focus (5–7 min)
4) Songwork with sheet music (10–15 min)
5) Rhetoric mini-performance or hymn reflection (3–5 min)
6) Assessment & stickers; note next step (2–3 min)

Each weekly plan contains an Age 3 adaptation and an Age 5 extension. If you only have time for 20–25 minutes, do steps 1–4 and mark partial completion.

### Materials
- A4 paper prints of weekly score(s) from `sheet_music/`
- Tuner or piano/keyboard app; metronome app set between 60–84 BPM
- Small props: scarf/ribbon (breath and phrasing), rhythm sticks or claps
- Water bottle

### Safety & Vocal Care
- Warm up gently; stop if there is strain or hoarseness.
- Encourage tall posture and relaxed shoulders; never "push" loud notes.
- Hydrate and schedule vocal rest if tired.

### Integrating Rhetoric (even at young ages)
- Tell the story of the song: “Who is singing? What are they saying?”
- Audience skills: face the listener, start together, finish with stillness and a smile.
- Sunday hymn reflection (optional): sing one hymn verse, discuss a word or image.

### How to Use the Files
- Begin with `Scope_and_Sequence.md` to place the week.
- Open `Weekly_Sessions.md` to run the exact plan.
- Open the listed `.ly` file in `sheet_music/` and print a PDF (see `sheet_music/README.md`).
- Check off the week in `Progress_Tracker.md`.

### Assessment
- Micro-milestones are embedded in each week (pitch match, steady beat, diction, memory, expression).
- Use the tracker to mark "met" or "in progress" and add brief notes.

---

<!-- Scope_and_Sequence.md -->

### Progression Map (Skill-Based, Not Time-Based)

Use this ordered path of skills and repertoire. Move forward when checkpoints are met. Age ranges indicate typical readiness but are flexible.

Legend: [A3] Age 3 adaptation | [A5] Age 5 extension | [Score] filename in `sheet_music/`

#### Level A — Foundations (Typical ages 3–5)
- A1 Posture & Breath; Do–So echo — Twinkle (phrase A) — `Twinkle_Twinkle_simple_C.ly` [A3][A5]
- A2 Beat vs. Words — Mary Had a Little Lamb — `Mary_Had_a_Little_Lamb_C.ly` [A3][A5]
- A3 Echo Pitch & Simple Dynamics — Row, Row, Row Your Boat — `Row_Row_Row_Your_Boat_C.ly` [A3][A5]
- A4 Tall Vowel Diction — Jesus Loves Me (v1) — `Jesus_Loves_Me_C.ly` [A3][A5]
- A5 Five-Note Scale (do–so) — Solfège Patterns — `solfege_patterns_C_major.ly` [A3][A5]

#### Level B — Musical Building Blocks (Typical ages 4–6)
- B1 Phrase Shape — Skip to My Lou — `Skip_To_My_Lou_C.ly` [A3][A5]
- B2 Breath Timing — Amazing Grace (v1) — `Amazing_Grace_simple_C.ly` [A3][A5]
- B3 Round Basics — Frère Jacques (melody) — `Frere_Jacques_round_C.ly` [A3][A5]
- B4 Sing a Simple Round — Frère Jacques (2 voices) — `Frere_Jacques_round_C.ly` [A3][A5]
- B5 Rhythm Names (ta / ti-ti) — Twinkle (phrase B) — `Twinkle_Twinkle_simple_C.ly` [A3][A5]

#### Level C — Reading & Ensemble (Typical ages 5–7)
- C1 Read Note Steps C–G — Mary (full) — `Mary_Had_a_Little_Lamb_C.ly` [A5]
- C2 Dynamic Contrast (soft/medium) — Row — `Row_Row_Row_Your_Boat_C.ly` [A5]
- C3 Clear Consonants — Yankee Doodle — `Yankee_Doodle_C.ly` [A5]
- C4 Memory: Hymn Verse — Jesus Loves Me (no sheet) — `Jesus_Loves_Me_C.ly` [A3][A5]
- C5 Pitch Center & Tempo — Amazing Grace (steady) — `Amazing_Grace_simple_C.ly` [A5]

#### Level D — Expression & Harmony (Typical ages 6–8)
- D1 Interval Sense (do–mi, do–so) — Solfège — `solfege_patterns_C_major.ly`
- D2 Long Notes, Calm Breath — Mary (sustains) — `Mary_Had_a_Little_Lamb_C.ly`
- D3 Expressive Faces/Story — Home on the Range — `Home_On_The_Range_C.ly`
- D4 Round Accuracy & Balance — Row (entries) — `Row_Row_Row_Your_Boat_C.ly`
- D5 Notation Drill — 5-note warmups — `warmups_five_note_scale_C_major.ly`

#### Level E — Performance Readiness (Typical ages 7–9)
- E1 Simple Harmony with Parent (third above) — Frère Jacques — `Frere_Jacques_round_C.ly`
- E2 Confident Start/Finish — Any learned song — (any prior score)
- E3 Small Family Share — Choose 2–3 pieces — (any prior score)

Notes:
- [A3] Keep ranges within C4–E5; use movement for rhythm; shorter phrases.
- [A5] Introduce simple staff pointing, light harmony (a third above with parent), and first round entries.

---

<!-- Weekly_Sessions.md -->

### Progression Checkpoints (Run at Any Pace)

Each checkpoint is a self-contained mini-lesson you can complete in one sitting. Use the Age 3 adaptation and Age 5 extension as needed. Scores are in `sheet_music/`.

---

#### A1 — Posture, Breath, Do–So | Twinkle (phrase A)
- Materials: `Twinkle_Twinkle_simple_C.ly`, scarf, metronome 72 BPM
- 1) Welcome & posture — Stand tall, soft knees, long neck.
- 2) Breath game — "Smell the flower, blow the candle" with scarf.
- 3) Warmup — Hum on C, lip trills, siren C–G.
- 4) Technique — Do–so call/echo.
- 5) Songwork — Twinkle phrase A (C C G G A A G2). Soft vs. medium.
- 6) Rhetoric — Who is singing? Smile at endings. Bow.
- Assess: Pitch center on C/G; steady beat.
- Age 3: Only first 2 bars; clap beat while parent sings.
- Age 5: Point to notes on printout; speak lyrics in rhythm, then sing.

---

#### A2 — Beat vs. Words | Mary Had a Little Lamb
- Materials: `Mary_Had_a_Little_Lamb_C.ly`
- 1) Posture & breath
- 2) Warmup — 5-note scale C–G, vowels "ah–ee–oo" on C.
- 3) Technique — Clap beat while speaking lyrics.
- 4) Songwork — Sing two lines; practice soft consonants.
- 5) Rhetoric — Who is Mary? What is the story?
- Assess: Beat consistent, words clear.
- Age 3: Use pictures of lamb; sing slower.
- Age 5: Read simple rhythm (quarter/quarter/half in bar 2).

---

#### A3 — Echo Pitch, Dynamics | Row, Row, Row Your Boat
- Materials: `Row_Row_Row_Your_Boat_C.ly`
- 1) Breath — Balloon belly inhale, hiss 6 counts.
- 2) Warmup — Do–mi–so arpeggio; quiet vs. medium dynamics.
- 3) Technique — Echo 3-note patterns.
- 4) Songwork — Sing melody; experiment soft/loud contrasts.
- 5) Rhetoric — What does "merrily" sound like on your face/voice?
- Assess: Copy short pitch patterns; switch dynamics on cue.
- Age 3: Hum the tune first; use rowing motion.
- Age 5: Clap one-bar intro; enter on time.

---

#### A4 — Vowel Diction | Jesus Loves Me (v1)
- Materials: `Jesus_Loves_Me_C.ly`
- 1) Posture/breath
- 2) Warmup — Vowel chain on C: ah–eh–ee–oh–oo.
- 3) Technique — Speak text slowly, feel tall vowels.
- 4) Songwork — Sing v1; shape phrase endings.
- 5) Rhetoric — What does "love" mean? Sing with gentle face.
- Assess: Round vowels, relaxed jaw.
- Age 3: Sing last line only; sway.
- Age 5: Mark breaths with pencil.

---

#### A5 — 5-Note Scale | Solfège Motifs
- Materials: `Do_Re_Mi_simplified_C.ly` or `solfege_patterns_C_major.ly`
- 1) Breath — In 4, hiss out 8.
- 2) Warmup — Scale up/down on solfège.
- 3) Technique — Step vs. skip; hands move up/down.
- 4) Songwork — Sing motif slowly; point to notes.
- 5) Rhetoric — What is a "scale"? Draw a staircase.
- Assess: Accurate steps C–D–E–F–G; steady tempo.
- Age 3: Use colored stickers for do/re/mi.
- Age 5: Read note heads on staff for C–G.

---

#### B1 — Phrase Shape | Skip to My Lou
- Materials: `Skip_To_My_Lou_C.ly`
- Warmup — Gentle siren; do–so.
- Technique — Move scarf in a rainbow shape for long phrases.
- Songwork — Sing phrase; circle the highest note.
- Rhetoric — Who are you singing to? Smile in voice.
- Assess: Smooth connection across bars.
- A3: Shorten to first 4 bars.
- A5: Add light dynamic swell in middle of phrase.

---

#### B2 — Breath Timing | Amazing Grace (v1)
- Materials: `Amazing_Grace_simple_C.ly`
- Breath — Book belly inhale (standing), exhale on "sss".
- Warmup — Sustain "ah" for 4–6 counts.
- Technique — Plan breaths with pencil marks.
- Songwork — Sing line by line; no gasp between words.
- Rhetoric — What is "grace"? Sing calmly.
- Assess: Clean breaths at phrase ends.
- A3: One line at a time.
- A5: Try 6-count sustain on the longest note.

---

#### B3 — Round Basics | Frère Jacques (melody)
- Materials: `Frere_Jacques_round_C.ly`
- Warmup — Sing melody straight through.
- Technique — Count 1-bar intro.
- Songwork — Parent sings, child hums.
- Rhetoric — What is a round? Draw two lines starting at different times.
- Assess: Independent start without rushing.
- A3: Echo 2-bar fragments.
- A5: Point to entry bar on score.

---

#### B4 — Round Together | Frère Jacques (round)
- Materials: `Frere_Jacques_round_C.ly`
- Warmup — Melody confident.
- Technique — Parent enters, child follows 1 bar later.
- Songwork — Sing full round.
- Rhetoric — Listen to blend; face forward.
- Assess: Hold own part vs. other voice.
- A3: Try 2-bar round only.
- A5: Switch roles and re-run.

---

#### B5 — Rhythm Names | Twinkle (phrase B)
- Materials: `Twinkle_Twinkle_simple_C.ly`
- Warmup — Clap quarter vs. two eighths.
- Technique — Speak rhythm then sing.
- Songwork — Phrase B with steady beat.
- Rhetoric — Smile at cadence.
- Assess: Ta vs. ti-ti accurate.
- A3: Use footsteps for beat.
- A5: Read simple rhythm line.

---

Further checkpoints continue the same structure for Levels C–E as listed in `Scope_and_Sequence.md` (Progression Map). Repeat any checkpoint as needed until skills feel secure.

---

<!-- Parent_Scripts_Age3.md -->

### Parent Scripts — Age 3 (Bella)

Use short, cheerful language and lots of modeling. Keep ranges within C4–E5.

General opener:
- "Let’s stand tall like a tree. Soft knees, long neck. Nice!"
- "Smell the flower… blow the candle. Good breath!"

Checkpoint A1 (Twinkle phrase A):
- "Echo me: do–so. Again: do–so."
- "Let’s hum like a bee on this note (C)."
- "Can you clap while I sing? One-two, one-two."

Checkpoint A2 (Mary):
- "Speak the words with me, clap the beat."
- "Now sing it softly like a tiny kitten."

Checkpoint A3 (Row):
- "Your turn to echo my three notes. Ready?"
- "Show me a big happy face for ‘merrily.’"

Checkpoint A4 (Jesus Loves Me):
- "Make your mouth tall for ‘love’: loooove."
- "Sway while we sing."

Checkpoint A5 (Solfège):
- "Stickers say: do is red, re is orange, mi is yellow."
- "Step up, step down with your hands."

Behavior & pacing tips:
- Praise attempts: "I love how you tried that!"
- Keep transitions quick; switch activities every ~3 minutes.
- Water sip and a smile between items.

---

<!-- Parent_Scripts_Age5.md -->

### Parent Scripts — Age 5 (Piper)

Use clear cues and invite independence. Lightly introduce reading and simple harmony.

General opener:
- "Check posture: tall spine, relaxed shoulders. Find your quiet ready."
- "In 4… breathe low like filling a balloon. Hiss for 6 counts."

Checkpoint A1 (Twinkle):
- "Point to the first note head. Speak the rhythm, then sing."
- "Circle the cadence note where we finish."

Checkpoint A2 (Mary):
- "Clap quarters vs. two eighths. Which bar has ti-ti?"
- "Sing the second line from memory."

Checkpoint A3 (Row):
- "Count 1–2–3–enter. Start together."
- "Try medium vs. soft dynamics on ‘merrily.’"

Checkpoint A4 (Jesus Loves Me):
- "Mark breaths with dots. Keep jaw relaxed for tall vowels."
- "Tell me one word that the song makes you think about."

Checkpoint B3/B4 (Frère Jacques round):
- "I’ll start, you point to bar 2 and enter after one bar."
- "Hold your part even if you hear mine."

Checkpoint E1 (Simple Harmony):
- "Sing a third above me on these notes; I’ll keep melody."
- "Listen for blend, no shouting."

Performance habits:
- "Face the audience, breathe, begin boldly, still finish, friendly bow."
- "If we make a mistake: we keep going with a smile."

---

<!-- Progress_Tracker.md -->

### Progress Tracker (Levels & Checkpoints)

Mark completion by Level and Checkpoint. Use Notes to record strengths/next steps.

| Level | Checkpoint | Completed | Notes |
| --- | --- | --- | --- |
| A | A1 Posture & Breath; Do–So echo | [ ] | |
| A | A2 Beat vs. Words | [ ] | |
| A | A3 Echo Pitch & Simple Dynamics | [ ] | |
| A | A4 Tall Vowel Diction | [ ] | |
| A | A5 Five-Note Scale (do–so) | [ ] | |
| B | B1 Phrase Shape | [ ] | |
| B | B2 Breath Timing | [ ] | |
| B | B3 Round Basics | [ ] | |
| B | B4 Sing a Simple Round | [ ] | |
| B | B5 Rhythm Names (ta / ti-ti) | [ ] | |
| C | C1 Read Note Steps C–G | [ ] | |
| C | C2 Dynamic Contrast | [ ] | |
| C | C3 Clear Consonants | [ ] | |
| C | C4 Memory: Hymn Verse | [ ] | |
| C | C5 Pitch Center & Tempo | [ ] | |
| D | D1 Interval Sense (do–mi, do–so) | [ ] | |
| D | D2 Long Notes, Calm Breath | [ ] | |
| D | D3 Expressive Faces/Story | [ ] | |
| D | D4 Round Accuracy & Balance | [ ] | |
| D | D5 Notation Drill | [ ] | |
| E | E1 Simple Harmony with Parent | [ ] | |
| E | E2 Confident Start/Finish | [ ] | |
| E | E3 Small Family Share | [ ] | |

Milestones to watch:
- Pitch match on do–mi–so
- Steady beat while singing
- Clear vowels and consonants
- Sing one song from memory (Age 3)
- Sing two songs from memory and start a round (Age 5)
- Confident start note, bow, and finish