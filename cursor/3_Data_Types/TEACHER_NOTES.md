# Module 3 — Teacher Notes (Data Types)

## Time guide (flexible)

| Lesson | Time | File |
|--------|------|------|
| 3.1 Types + type() | 45–50 min | `3_1_data_types.py` |
| 3.2 Conversion | 55–70 min | `3_2_type_conversion.py` |
| 3.3 Errors | 40–45 min | `3_3_conversion_errors.py` |
| 3.4 bool extension | 20 min optional | `3_4_extension_bool.py` |
| Quiz | 45 min | `3_5_quiz.py` |

## Skipped here (Module 4)

Do **not** use old `code/3_Data_Types/3_4_basic_math_operators.py` through `3_7_f_string.py` in the same week — that duplicates Module 4.

| Old file topic | Teach in |
|----------------|----------|
| `+ - * / // %` | Module 4 |
| BODMAS | Module 4 |
| f-strings | Module 4 |

Simple `+` after `int()` in this module is only to **prove conversion works**.

## Bilingual anchors

| English | Urdu |
|---------|------|
| Data type | ڈیٹا ٹائپ |
| int | عدد صحیح |
| float | اعشاریہ |
| Convert | تبدیل کرنا |
| TypeError | ٹائپ غلطی |
| ValueError | value غلط |

## Demo order for TypeError

1. Uncomment `print("Age: " + years)` in `3_1` — show red error.
2. Fix with `str()` and with comma — students see two fixes.

## Common student mistakes

| Mistake | Teaching response |
|---------|-------------------|
| `int(input())` when user types `12.5` | Use `float()` first |
| `int("12 years")` | Only digits allowed in basic `int()` |
| Thinks `int(89.9)` rounds to 90 | It **truncates** to 89 — say “cuts off decimal” |
| `bool("False")` is False | Extension only: non-empty str is True |

## Mixed audience examples

Alternate rows: **ajza / Maktaba** and **class strength / cricket score / rupees**.

## Lab note

When two `input()` in one file, students must answer **both** prompts in Terminal before output appears.

## Extension

- `isdigit()` validation — included in 3.3; good habit before `int()`.
- Full `try/except` — not in this course level; keep validation simple.
