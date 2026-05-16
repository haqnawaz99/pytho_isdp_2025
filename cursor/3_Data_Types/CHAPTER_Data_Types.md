# Module 3: Data Types and Type Conversion

**Prerequisites:** Module 2 (variables, `input()`, `len()`, `str()` with `+`)  
**This module does NOT include:** full math operators, BODMAS, f-strings — those are **Module 4**.

---

## Module learning objectives

Students will be able to:

1. Name the four main types: **int**, **float**, **str**, **bool**.
2. Use **`type()`** to check a value’s type.
3. Convert with **`int()`**, **`float()`**, and **`str()`** when needed.
4. Convert **`input()`** text to numbers for simple calculations.
5. Recognize common **TypeError** and **ValueError** and fix them.

> **Urdu:** ڈیٹا ٹائپ بتاتی ہے value کس قسم کی ہے۔ `input()` ہمیشہ string دیتا ہے — گنتی کے لیے `int()` یا `float()` چاہیے۔

---

## Lesson 3.1 — Data types and `type()`

### Concept

Every value in Python has a **data type**. At this level we focus on four:

| Type | Meaning | Examples |
|------|---------|----------|
| **int** | Whole number | `17`, `1200`, `30` |
| **float** | Decimal number | `12.99`, `36.5` |
| **str** | Text in quotes | `"Lahore"`, `"Quran"` |
| **bool** | True or False | `True`, `False` (capital letters) |

Check type with **`type(value)`**:

```python
age = 17
print(type(age))    # <class 'int'>

price = 250.50
print(type(price))  # <class 'float'>

name = "Ahmed"
print(type(name))   # <class 'str'>

is_student = True
print(type(is_student))  # <class 'bool'>
```

### Pakistan / school examples

```python
students_in_class = 35
print("Students:", students_in_class)

temperature_c = 38.5
print("Temperature:", temperature_c)

city = "Karachi"
print("City:", city)

fee_paid = False
print("Fee paid:", fee_paid)
```

### Large numbers (readable)

```python
population = 220_000_000
print("Pakistan population (approx):", population)
```

Underscores are only for **reading**; Python treats it as one integer.

### Mixing str and int with `+` (error)

```python
age = 17
# print("Your age is: " + age)   # TypeError — cannot add str and int
print("Your age is: " + str(age))  # OK
print("Your age is:", age)          # OK — comma in print
```

**Lists, dictionaries:** We meet them in **Module 7**. Not required here.

**File:** `3_1_data_types.py`

---

## Lesson 3.2 — Type conversion

### Why convert?

- `input()` → always **str** (text).
- To **add numbers** typed by the user → `int()` or `float()`.
- To **join number in a sentence** with `+` → `str()`.

### `int()` — string to whole number

```python
num_str = "25"
num_int = int(num_str)
print(num_int + 5)   # 30
```

### `float()` — string to decimal

```python
price_str = "12.75"
price_float = float(price_str)
print(price_float + 2.25)
```

### `str()` — number to text

```python
students = 30
print("Total students: " + str(students))
```

### `float` → `int` (drops decimal part)

```python
marks = 89.9
print(int(marks))   # 89
```

### `input()` + conversion

```python
user_input = input("Enter a whole number: ")
num = int(user_input)
print("You entered:", num)
print("Double:", num + num)
```

Two numbers:

```python
a = int(input("First number: "))
b = int(input("Second number: "))
print("Sum:", a + b)
```

### Decimal input (two steps)

`int("45.6")` fails. Use `float` first, then `int` if you need a whole number:

```python
height_str = "172.5"
height_float = float(height_str)
height_int = int(height_float)
print(height_int)   # 172
```

### Madrasa / daily life examples

```python
ajza = int(input("How many ajza memorized? "))
print("MashaAllah, you have memorized", ajza, "ajza")

rupees_str = input("Book price in rupees: ")
rupees = float(rupees_str)
print("Price:", rupees)
```

**File:** `3_2_type_conversion.py`  
**Checkpoint:** Program asks age as input, converts to int, prints age + 1 (next birthday).

---

## Lesson 3.3 — Common errors and fixes

| Error | Cause | Fix |
|-------|-------|-----|
| **TypeError** | `"text" + 5` or `input_num + 5` without `int()` | Convert or use comma in `print` |
| **ValueError** | `int("abc")`, `int("")`, `int("12.5")` | Valid numeric text; use `float` first for decimals |
| **ValueError** | `int("12 years")` | Extract digits only or ask again |

### Examples

```python
# Fix TypeError
age = 20
print("You are " + str(age) + " years old.")

# Fix ValueError — use valid string
number = int("123")
print(number)

# Fix input without conversion
num = int(input("Enter a number: "))
print(num + 10)

# Decimal string to int
value = int(float("45.6"))
print(value)
```

### Empty or bad input (simple check)

```python
text = input("Enter a whole number: ")
if text.isdigit():
    n = int(text)
    print("Thank you, you entered", n)
else:
    print("Please enter digits only, e.g. 25")
```

**File:** `3_3_conversion_errors.py`

---

## Lesson 3.4 — Extension: `bool()` (optional)

```python
print(bool(""))       # False — empty string
print(bool("hello"))  # True — non-empty string
print(bool(0))        # False
print(bool(7))        # True
```

Non-empty strings are `True` even if text is `"False"`. Use only when needed.

**File:** `3_4_extension_bool.py`

---

## Lesson 3.5 — Quiz

**Files:** `3_5_quiz.py`, `3_6_solutions.py`

---

## Summary

| Function | Use |
|----------|-----|
| `type(x)` | What type is `x`? |
| `int(x)` | Whole number |
| `float(x)` | Decimal number |
| `str(x)` | Text for concatenation |

**Next module:** Operators (math, comparison, logical) and **f-strings**.
