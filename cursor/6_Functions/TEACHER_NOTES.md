# Module 6 — Teacher Notes (Functions)

## Time guide (flexible)

| Lesson | Time | File |
|--------|------|------|
| 6.1 Basic def/call | 45 min | `6_1_basic_functions.py` |
| 6.2 Parameters | 50 min | `6_2_parameters.py` |
| 6.3 return | 55 min | `6_3_return_values.py` |
| 6.4 Defaults | 40 min | `6_4_default_parameters.py` |
| Quiz | 50–60 min | `6_5_quiz.py` |

## Key teaching moves

### Define before call

Show error: call `say_hi()` before `def say_hi()` — NameError.

### return vs print

| Student writes | Issue |
|----------------|-------|
| `def add(a,b): print(a+b)` | No value to store |
| `def add(a,b): return a+b` | Can use `x = add(2,3)` |

Demo both side by side.

### Default parameter order

Wrong: `def f(a=1, b):` — syntax error.  
Right: `def f(b, a=1):`

## Skip from old folder

- `6_5_string_methods.py` — review only; not a new topic (Module 1).
- `6_8_islamic_function_applications.py` — too long for one lesson; use capstone instead.

## Bilingual

| English | Urdu |
|---------|------|
| Function | فنکشن |
| Parameter | پیرامیٹر / وسیلہ |
| Return | واپس کرنا |
| Call | چلانا |

## Common errors

| Error | Fix |
|-------|-----|
| Forgot `()` on call | `say_salam` vs `say_salam()` |
| Missing colon after def | `def f():` |
| No indent under def | Same as if-block |
| `return` after print only path | One return path per simple function OK for beginners |

## Extension

- Function that calls another function.
- Combine with `input`: `name = input(); greet(name)`.

## Link to Module 7

“Lists let us pass many values; soon we will loop over them in functions too.”
