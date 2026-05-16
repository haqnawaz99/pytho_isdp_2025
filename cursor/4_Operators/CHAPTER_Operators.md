# Module 4: Operators (Math, Comparison, Logical, f-strings)

**Prerequisites:** Module 3 (types, `int()`, `float()`, `str()`)  
**Next:** Module 5 uses comparison/logical results inside `if` statements.

---

## Module learning objectives

Students will be able to:

1. Use math operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
2. Apply **BODMAS** and **brackets** `()`.
3. Compare values with `==`, `!=`, `<`, `>`, `<=`, `>=` (get `True`/`False`).
4. Combine booleans with `and`, `or`, `not`.
5. Build messages with **f-strings**.

> **Urdu:** آپریٹر symbols ہیں جو حساب یا موازنہ کرتے ہیں۔ `//` ہر ایک کو برابر حصہ، `%` بچا ہوا حصہ۔

---

## Lesson 4.1 — Mathematical operators

### Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Add | `5 + 3` → 8 |
| `-` | Subtract | `10 - 4` → 6 |
| `*` | Multiply | `6 * 4` → 24 |
| `/` | Divide (float) | `12 / 4` → 3.0 |
| `//` | Floor divide (whole part) | `25 // 3` → 8 |
| `%` | Remainder | `25 % 3` → 1 |
| `**` | Power | `2 ** 3` → 8 |

### `/` vs `//` vs `%`

Distributing **28 notebooks** among **5 students**:

- Each gets: `28 // 5` → 5  
- Leftover: `28 % 5` → 3  

Use `//` and `%` for physical items; `/` gives decimals.

### Programs

```python
item_price = 250
quantity = 6
total = item_price * quantity
print("Total rupees:", total)
```

```python
qurans = 28
shelves = 5
print("Per shelf:", qurans // shelves)
print("Leftover:", qurans % shelves)
```

**File:** `4_1_math_operators.py`

---

## Lesson 4.2 — BODMAS and brackets

Order (like school maths):

1. **B**rackets `( )`
2. **O**rders `**`
3. **M**ultiply / **D**ivide (left to right)
4. **A**dd / **S**ubtract (left to right)

```python
print(10 + 5 * 3)      # 25
print((10 + 5) * 3)    # 45
print(2 * 3 ** 2)      # 18
```

```python
budget = 5000
spent = (850 * 2) + 600
left = budget - spent
print("Left:", left)
```

**File:** `4_2_bodmas.py`

---

## Lesson 4.3 — Comparison operators

Compare two values → **bool** (`True` or `False`).

| Operator | Meaning |
|----------|---------|
| `==` | equal |
| `!=` | not equal |
| `>` `<` | greater / less |
| `>=` `<=` | greater-or-equal / less-or-equal |

```python
print(15 >= 10)
print(8 < 10)
print("Lahore" == "Lahore")
print("Fajr" != "Isha")
```

Store result:

```python
marks = 68
passed = marks >= 70
print("Passed:", passed)
```

Age range (two comparisons — combine with `and` in 4.4):

```python
age = 12
print(age >= 10)
print(age <= 15)
```

**Important:** `=` assigns; `==` compares.

**File:** `4_3_comparison_operators.py`

---

## Lesson 4.4 — Logical operators

Work on **True/False** only.

| Operator | Meaning |
|----------|---------|
| `and` | Both True → True |
| `or` | At least one True → True |
| `not` | Flip True ↔ False |

```python
has_attended = True
has_homework = False
print(has_attended and has_homework)
print(has_attended or has_homework)
print(not has_homework)
```

Combine with comparisons:

```python
age = 14
in_teens = age >= 10 and age <= 19
print("Teen:", in_teens)

marks = 75
passed = marks >= 50
print("Passed:", passed)
```

Eligibility example:

```python
attended = True
homework = False
read_quran = True
eligible = attended and (homework or read_quran)
print("Eligible:", eligible)
```

**File:** `4_4_logical_operators.py`  
*Module 5 will use these inside `if`.*

---

## Lesson 4.5 — f-strings

Put `f` before quotes; `{variable}` or `{expression}` inside:

```python
name = "Ahmed"
print(f"My name is {name}")

age = 15
print(f"{name} is {age} years old.")
```

With maths:

```python
price = 170
kg = 5
print(f"{kg} kg costs {price * kg} rupees.")
```

With input:

```python
city = input("Your city? ")
print(f"I live in {city}.")
```

**File:** `4_5_f_strings.py`

---

## Lesson 4.6 — Quiz

**Files:** `4_6_quiz.py`, `4_7_solutions.py`

---

## Summary

| Topic | Symbols / syntax |
|-------|------------------|
| Math | `+ - * / // % **` |
| Order | BODMAS, `( )` |
| Compare | `== != < > <= >=` |
| Logic | `and or not` |
| f-string | `f"...{x}..."` |

**Next:** Control flow — `if`, `else`, loops.
