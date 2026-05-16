# Module 2: Variables and Input

**Prerequisites:** Module 0 (`print`), Module 1 (strings, concatenation, string methods)  
**This module does NOT include:** math operators, BODMAS, f-strings, or `int()` conversion — those are Modules 3 and 4.

---

## Module learning objectives

Students will be able to:

1. Explain what a **variable** is and assign a value with `=`.
2. Use **clear variable names** following Python rules (snake_case).
3. Store text from **`input()`** in a variable and use it in messages.
4. Use **`len()`** on a variable and print the result with `str()` or a comma in `print()`.
5. *(Optional)* Apply string **methods** from Module 1 to values held in variables.

> **Urdu:** متغیر (variable) ایک نام ہے جو میموری میں value رکھتا ہے۔ `input()` سے جو لکھیں وہ ہمیشہ **string** ہوتی ہے — اگلے ماڈیول میں numbers پر بات کریں گے۔

---

## Lesson 2.1 — Variables and assignment

### Concept

A **variable** is a **name** for a value stored in the computer. We **assign** with `=`:

```python
name = "Ahmed"
```

Read as: “`name` holds the string `Ahmed`.”  
The **name** is on the left; the **value** is on the right.

We use variables so we do not repeat the same text many times, and so we can use **input** later.

### String variables

```python
greeting = "Assalamu Alaikum"
print(greeting)

name = "Fatima"
print("My name is " + name)

city = "Multan"
print("I live in " + city)
```

### Joining two variables

```python
first_name = "Hafiz"
last_name = "Usman"
print(first_name + " " + last_name)
```

### Pakistan and madrasa examples

```python
school = "Government Girls High School Lahore"
print(school)

favourite_sport = "cricket"
print("I love " + favourite_sport)

madrasa = "Jamia Ashrafia"
print("I study at " + madrasa)
```

### Storing numbers (display only — maths in Module 4)

You may store a whole number **without quotes** to use later:

```python
class_number = 7
print("Class:", class_number)
```

Do not use `+` to join text and this number yet — use a **comma** in `print` (see Lesson 2.3) or wait for `str()` in Module 3.

### Common mistakes

| Mistake | Fix |
|---------|-----|
| `Name = "Ali"` then `print(name)` | Names are **case-sensitive** — same spelling |
| `print(age)` before `age = 14` | **Assign first**, then use |
| `name = Ahmed` | Text needs quotes: `"Ahmed"` |

**File:** `2_1_assignment_and_strings.py`  
**Checkpoint:** Three variables (name, city, hobby) printed in one sentence with `+`.

---

## Lesson 2.2 — `input()` and string variables

### Concept

`input("prompt")` shows a message, waits for the user to type, and returns what they typed as a **string**. Always store it in a variable if you need it again.

```python
name = input("What is your name? ")
print("Welcome " + name)
```

### More examples (mixed context)

```python
city = input("Which city do you live in? ")
print("You live in " + city)

subject = input("Enter your favourite subject: ")
print("You like " + subject)

book = input("Enter your favourite book: ")
print("You like the book " + book)

madrasa = input("What is your madrasa or school name? ")
print("You study at " + madrasa)
```

### Two inputs in one program

```python
friend1 = input("First friend name: ")
friend2 = input("Second friend name: ")
print("Friends: " + friend1 + " and " + friend2)
```

### Important

- Whatever the user types (even `17`) is stored as **text** until we learn conversion in **Module 3**.
- Run the program in VS Code; type in the **Terminal** when the cursor waits.

**File:** `2_2_input.py`  
**Checkpoint:** Program asks name and favourite food; prints both in one line.

---

## Lesson 2.3 — `len()` with variables

### Concept

From Module 1 you know `len("Lahore")`. The same works on a variable that holds a string:

```python
name = "Ahmed"
print(len(name))
```

To **combine** a message with the length using `+`, convert the number to string:

```python
name = input("Enter your name: ")
print("Characters in your name: " + str(len(name)))
```

### Easier way — comma in `print()`

```python
name = input("Enter your name: ")
name_length = len(name)
print("Number of letters:", name_length)
```

The comma adds a space and allows mixing text and numbers **without** `str()`.

### Examples

```python
surah = input("Enter a Surah name: ")
print("Length:", len(surah))

school_name = "Sindh Madressatul Islam"
print("Letters in school name:", len(school_name))
```

**File:** `2_3_len_with_variables.py`  
**Checkpoint:** Ask for city name; print length using comma or `str(len(...))`.

---

## Lesson 2.4 — Variable naming rules

### Rules (must follow)

- Letters, digits, underscore `_` only (no spaces).
- **Cannot start with a digit** — `student1` OK, `1student` error.
- **No hyphens** — use `student_name` not `student-name`.
- **Not a Python keyword** — use `student_class` not `class`.

### Convention (recommended — PEP 8)

- **snake_case:** `full_name`, `total_books`, `favourite_city`
- Name should **describe** the value: `city` better than `x`

### Examples

```python
full_name = "Ayesha Khan"
student_class = "Grade 6"
subject_name = "Quran"
books_in_maktaba = 120
```

**File:** `2_4_naming_rules.py`  
**Checkpoint:** Fix three bad names on paper; write one correct program with `snake_case`.

---

## Lesson 2.5 — Extension: string methods with variables

Apply Module 1 methods to variables (especially after `input()`):

```python
city = input("Enter city: ")
print(city.strip().title())

message = "  assalamu alaikum  "
clean = message.strip().title()
print(clean)
```

**File:** `2_5_string_methods_with_variables.py` (optional)

---

## Lesson 2.6 — Quiz

**Files:** `2_6_quiz.py`, `2_7_solutions.py`  
**Assessment:** see `ASSESSMENT.md`

---

## Exercise set (summary)

### Set A — Assignment

1. Variable `greeting` = `"Assalamu Alaikum"`, print it.  
2. Variables `first` and `last`, print full name with space.  
3. Variable `city` = your city, print `"I live in "` + city.

### Set B — Input

1. Ask name; print welcome.  
2. Ask favourite sport; print one sentence.  
3. Ask school or madrasa name; print where you study.

### Set C — len and naming

1. Ask for a word; print its length (comma or `str`).  
2. List three rules for variable names.  
3. Why is `student name` invalid?

**Solutions:** `2_7_solutions.py`

---

## Summary

| Term | Meaning |
|------|---------|
| Variable | Named storage for a value |
| Assignment | `name = value` |
| `input()` | Read text from user (always string) |
| Case-sensitive | `Name` and `name` are different |
| snake_case | lowercase_with_underscores |

**Next module:** Data types (`int`, `float`, `bool`) and type conversion (`int()`, `str()`).
