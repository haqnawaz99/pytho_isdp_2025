# Module 7: Lists, Tuples, Sets, and Dictionaries

**Prerequisites:** Modules 5–6 (loops, functions)  
**Connects to:** Module 1 `.split()` / `.join()` now makes more sense with lists.

---

## Module learning objectives

Students will be able to:

1. Create a **list**, access items by **index**, use `len()`.
2. Modify lists with **`.append()`**, **`.remove()`**, **`.sort()`**, and loop with `for`.
3. Explain **tuple** (fixed) and **set** (unique items) at a basic level.
4. Use **dictionaries** with keys and values; access with `[]` and `.get()`.
5. Work with a **simple nested** structure (list of student records).

> **Urdu:** لسٹ = ایک ترتیب والا ڈبہ۔ ڈکشنری = چابی (key) اور قیمت (value) کا جوڑا۔

---

## Lesson 7.1 — Lists and indexing

### Concept

A **list** holds multiple items in order, in square brackets `[]`:

```python
prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
cities = ["Lahore", "Karachi", "Islamabad"]
marks = [85, 92, 78, 90]
```

### Index (position)

Starts at **0**:

```python
print(prayers[0])   # first
print(prayers[2])   # third
print(prayers[-1])  # last
```

```python
print(len(prayers))
```

**File:** `7_1_basic_lists.py`

---

## Lesson 7.2 — List methods and loops

```python
books = ["Quran", "Hadith"]
books.append("Fiqh")
print(books)

books.remove("Hadith")
print(books)

numbers = [30, 10, 50]
numbers.sort()
print(numbers)
```

Loop (Module 5):

```python
subjects = ["Math", "Urdu", "Science"]
for subject in subjects:
    print(f"Lesson: {subject}")
```

**File:** `7_2_list_methods.py`

---

## Lesson 7.3 — Tuples and sets (introduction)

### Tuple `()` — cannot change after creation

```python
prayer_count = (5,)  # one item tuple needs comma
colors = ("green", "white")
print(colors[0])
```

### Set `{}` — unique items, no duplicates

```python
unique_cities = {"Lahore", "Karachi", "Lahore"}
print(unique_cities)
```

**File:** `7_3_tuples_and_sets.py` (short intro only)

---

## Lesson 7.4 — Dictionaries

**Key → value** pairs with `{ }`:

```python
student = {
    "name": "Ahmed",
    "age": 15,
    "city": "Multan"
}
print(student["name"])
print(student.get("age"))
```

Add or change:

```python
student["grade"] = 88
```

Loop:

```python
for key in student:
    print(key, student[key])
```

**File:** `7_4_dictionaries.py`

---

## Lesson 7.5 — Simple nested data

List of dictionaries — many students:

```python
class_list = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Hassan", "marks": 76}
]

for pupil in class_list:
    print(f"{pupil['name']}: {pupil['marks']}")
```

Dictionary containing a list:

```python
school = {
    "name": "Al-Noor School",
    "city": "Karachi",
    "subjects": ["Math", "Urdu", "Islamiat"]
}
print(school["subjects"][0])
```

**File:** `7_5_nested_data.py`

---

## Lesson 7.6 — Quiz

**Files:** `7_6_quiz.py`, `7_7_solutions.py`

---

## Summary

| Structure | Syntax | Mutable? |
|-----------|--------|----------|
| List | `[ ]` | Yes |
| Tuple | `( )` | No |
| Set | `{ }` unique | Yes |
| Dict | `{key: value}` | Yes |

**Next module:** Mini projects combining all topics.
