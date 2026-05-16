# Module 6: Functions

**Prerequisites:** Modules 2–5 (variables, types, operators, `if`, loops)  
**Idea:** Write instructions **once**, use them **many times**.

---

## Module learning objectives

Students will be able to:

1. Define a function with `def` and **call** it.
2. Pass **parameters** into a function.
3. **Return** a value from a function and use it.
4. Use **default parameters** when an argument is optional.

> **Urdu:** فنکشن وہ بلاک ہے جو ایک نام سے بار بار چلایا جا سکتا ہے۔ `return` سے جواب واپس ملتا ہے۔

---

## Lesson 6.1 — Define and call (no parameters)

### Concept

A **function** is a named block of code. We **define** it with `def`, then **call** it by name with `()`.

```python
def say_salam():
    print("Assalamu Alaikum")

say_salam()
say_salam()
```

Rules:

- `def` line ends with **colon** `:`  
- Body is **indented** (like `if`)  
- Call **after** the function is defined (in the same file)

### Function vs method

- **Our function:** `def my_function():`  
- **String method** (Module 1): `"hi".upper()` — already built into Python

**File:** `6_1_basic_functions.py`

---

## Lesson 6.2 — Parameters

**Parameters** send data into the function:

```python
def greet_person(name):
    print(f"Assalamu Alaikum {name}")

greet_person("Ahmed")
greet_person("Fatima")
```

```python
def show_city(city):
    print(f"I love {city}")

show_city("Lahore")
show_city("Multan")
```

```python
def print_total(price, quantity):
    total = price * quantity
    print(f"Total rupees: {total}")

print_total(250, 4)
```

Multiple parameters: order matters — `print_total(250, 4)` not `(4, 250)` unless names match.

**File:** `6_2_parameters.py`

---

## Lesson 6.3 — Return values

`return` sends a value **back** to the caller:

```python
def get_greeting():
    return "Assalamu Alaikum"

msg = get_greeting()
print(msg)
```

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print(result)
```

```python
def passed_test(marks):
    return marks >= 50

print(passed_test(72))
print(passed_test(40))
```

Use return for **calculations**; use `print` inside function only when you want to show on screen directly.

**File:** `6_3_return_values.py`

---

## Lesson 6.4 — Default parameters

If caller omits an argument, the **default** is used:

```python
def greet(name="Student"):
    print(f"Welcome, {name}")

greet("Ahmed")
greet()
```

```python
def book_price(quantity, price_per_book=100):
    return quantity * price_per_book

print(book_price(5))
print(book_price(3, 250))
```

Defaults must come **after** required parameters.

**File:** `6_4_default_parameters.py`

---

## Lesson 6.5 — Quiz

**Files:** `6_5_quiz.py`, `6_6_solutions.py`

---

## Summary

| Term | Meaning |
|------|---------|
| `def` | Start function definition |
| Parameter | Variable in `def` line |
| Argument | Value passed when calling |
| `return` | Give result back |
| Default | Value used if argument missing |

**Next module:** Lists and dictionaries.
