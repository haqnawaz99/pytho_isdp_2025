# Module 7 — Teacher Notes (Lists & Dictionaries)

## Time guide (flexible)

| Lesson | Time | File |
|--------|------|------|
| 7.1 Lists + index | 50 min | `7_1_basic_lists.py` |
| 7.2 Methods + loops | 55 min | `7_2_list_methods.py` |
| 7.3 Tuple/set intro | 30 min | `7_3_tuples_and_sets.py` |
| 7.4 Dictionaries | 55 min | `7_4_dictionaries.py` |
| 7.5 Nested | 50 min | `7_5_nested_data.py` |
| Quiz | 60 min | `7_6_quiz.py` |

## Pedagogy

1. **Module 1 callback:** Show `"a,b,c".split(",")` again — now students know it is a list.
2. **Index 0:** Draw list boxes 0,1,2 on board — biggest confusion point.
3. **Dict vs list:** List = ordered items by number; dict = look up by **name** (key).

## Do NOT use in class (yet)

- `code/7_Lists/7_7_islamic_applications.py` — nested departments; too large.
- List comprehensions, `.pop()`, `.extend()` — optional extension only.
- `try/except` for tuple immutability — explain in words instead.

## Common errors

| Error | Fix |
|-------|-----|
| `list[1]` when only 1 item | IndexError — check len |
| `dict["wrong_key"]` | KeyError — use `.get()` |
| `set` order changes | Sets unordered — normal |
| Confuse `{}` empty dict vs set | `{}` is dict; set needs `set()` or `{"a"}` |

## Bilingual

| English | Urdu |
|---------|------|
| List | فہرست / لسٹ |
| Index | انڈیکس / نمبر |
| Dictionary | لغت / ڈکشنری |
| Key | چابی |
| Value | قیمت |

## Extension

- Function that takes a list and returns average of marks list.
- Save class_list to a simple report with f-strings.

## After this module

Module 8 projects tie everything together.
