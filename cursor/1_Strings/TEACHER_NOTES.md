# Module 1 — Teacher Notes (Strings)

## Time guide (flexible)

| Lesson | Time | File |
|--------|------|------|
| 1.1 Concatenation, len | 45–60 min | `1_1_concatenation.py` |
| 1.2 Methods (core) | 50–70 min | `1_2_string_methods.py` |
| 1.3 Escape sequences | 30–40 min | `1_3_escape_sequences.py` |
| 1.4 Extension | 30 min optional | `1_4_extension_methods.py` |
| 1.5 Quiz | 40–50 min | `1_5_quiz.py` |

## Bilingual delivery (Urdu + English)

Suggested pattern each concept:

1. Say term in English on board: **concatenation**
2. Urdu meaning: **جوڑنا** — strings ko `+` se jorna
3. Live code — students type same file
4. One Pakistan example + one Islamic example (alternate rows in file)

Keep **code 100% English** even when explaining in Urdu.

## Mixed madrasa + school

- Use **both** “Jamia / Maktaba” and “school / class / section” in examples — not only one world.
- Extension lesson (1.4) can be homework for schools with more periods; madrasa classes can skip until Module 7.

## Common misconceptions

| Mistake | Response |
|---------|----------|
| `.upper()` “changes” the original | Demo: `s = "hi"` not used yet — show immutability with two prints |
| `len` is a method | `len()` is a **function** — parentheses required |
| `\n` prints as two characters on screen | Run once — shows one newline in output |
| Confuse `+` with math | In quotes, `+` joins text; numbers come in Module 3 |

## Sensitive points

- Religious text in `print()` is for **literacy**, not testing belief.
- Avoid jokes about names or madaris.

## Extensions

- Run **`1_urdu_strings.py`** (adopted from claude) for bilingual classes.
- Print student list from hard-coded strings (preview of lists).
- Compare `.capitalize()` vs `.title()` on same string side by side.
- Printable homework: `practice_sheets/module_1_practice.md`

## Link to original materials

Chapter text aligns with `code/1_Strings/CHAPTER_Strings.md` but splits **core vs extension** and adds lesson files. Diagrams from original folder can be copied into `cursor/1_Strings/diagrams/` later if needed for slides.
