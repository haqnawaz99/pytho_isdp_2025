# Module 5: Control Flow (if, else, elif, loops)

**Prerequisites:** Module 4 (comparisons, `and`/`or`/`not`, f-strings)  
**Note:** We **use** operators from Module 4 inside `if` — we do not re-teach them here.

---

## Module learning objectives

Students will be able to:

1. Run code **only when a condition is True** using `if`.
2. Choose between two paths with `if` / `else`.
3. Choose among many paths with `elif`.
4. Repeat code with `while` and `for` loops.
5. Use `range()` and loop over a **list** of items.

> **Urdu:** `if` کا مطلب “اگر شرط سچ ہو تو یہ کوڈ چلاؤ”۔ انڈینٹ (spaces) ضروری ہے — عام طور پر 4 spaces۔

---

## Lesson 5.1 — `if` statements

### Syntax

```python
if condition:
    # indented block — runs only if condition is True
```

The line after `if` ends with **colon** `:`  
The next lines must be **indented** (4 spaces).

### Examples

```python
is_student = True
if is_student:
    print("Keep learning!")
```

```python
marks = 75
if marks >= 50:
    print("You passed.")
```

```python
city = input("Your city? ")
if city == "Lahore":
    print("You are from Lahore.")
```

```python
age = 14
if age >= 10 and age <= 18:
    print("Teen student.")
```

**File:** `5_1_if.py`

---

## Lesson 5.2 — `if` / `else`

When condition is False, run the **else** block:

```python
marks = 45
if marks >= 50:
    print("Passed")
else:
    print("Need more study")
```

```python
fee_paid = input("Fee paid? (yes/no): ")
if fee_paid == "yes":
    print("Thank you.")
else:
    print("Please pay at the office.")
```

Use **respectful** prompts — not to embarrass students.

**File:** `5_2_if_else.py`

---

## Lesson 5.3 — `elif` (else-if)

Many choices — check top to bottom; **first True wins**:

```python
time_of_day = "evening"
if time_of_day == "morning":
    print("Good morning")
elif time_of_day == "afternoon":
    print("Good afternoon")
elif time_of_day == "evening":
    print("Good evening")
else:
    print("Good night")
```

```python
score = int(input("Enter marks: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")
```

**File:** `5_3_elif.py`

---

## Lesson 5.4 — `while` loops

Repeat **while** condition is True:

```python
count = 1
while count <= 5:
    print("Count:", count)
    count = count + 1
```

Shorthand: `count += 1` means `count = count + 1`.

### Example — count prayers / repetitions

```python
n = 1
while n <= 5:
    print(f"Step {n}")
    n += 1
```

### Example — study minutes

```python
minutes = 0
while minutes < 30:
    print(f"Studied {minutes} minutes")
    minutes += 10
```

**Warning:** If the condition never becomes False, loop runs forever (infinite loop). Always change the variable inside the loop.

**File:** `5_4_while_loops.py`  
**Extension:** `break` stops loop early (see teacher notes).

---

## Lesson 5.5 — `for` loops

### `range()`

```python
for i in range(1, 6):
    print(i)
```

Prints 1, 2, 3, 4, 5 (6 is **not** included).

```python
for x in range(5):
    print(x)
```

Prints 0, 1, 2, 3, 4.

### Loop over a list

```python
subjects = ["Math", "Urdu", "Science", "Islamiat"]
for subject in subjects:
    print(f"Studying {subject}")
```

```python
cities = ["Lahore", "Karachi", "Islamabad"]
for city in cities:
    print(city)
```

### Loop over a string (each character)

```python
word = "Pakistan"
for letter in word:
    print(letter)
```

**File:** `5_5_for_loops.py`

---

## Lesson 5.6 — Quiz

**Files:** `5_6_quiz.py`, `5_7_solutions.py`

---

## Indentation rules (summary)

```python
if marks >= 50:
    print("Pass")      # inside if
    print("Well done") # inside if
print("Done")          # outside if — always runs
```

---

## Summary

| Statement | Use |
|-----------|-----|
| `if` | One path when True |
| `else` | Other path when False |
| `elif` | Many paths |
| `while` | Repeat while condition True |
| `for` | Repeat for each item / number in range |

**Next module:** Functions — reusable blocks of code.
