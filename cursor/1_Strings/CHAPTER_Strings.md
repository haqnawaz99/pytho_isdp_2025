# Module 1: Strings in Python

**Prerequisite:** Module 0 (`print`, comments, run files in VS Code)  
**Rule for this module:** Use **string literals** (text in quotes). **No variables yet** — that is Module 2.

---

## Module learning objectives

Students will be able to:

1. Define a **string** and create it with `'` or `"` quotes.
2. **Concatenate** strings with `+` and use `len()`.
3. Use core **string methods**: `.upper()`, `.lower()`, `.title()`, `.strip()`, `.replace()`.
4. Format output with escape sequences `\n` and `\t`.
5. *(Extension)* Use `.split()`, `.join()`, `.startswith()`, `.find()` — optional for faster groups.

> **Urdu:** سٹرنگ متن ہے جو quotes میں لکھتے ہیں۔ `+` سے جوڑنا **concatenation** کہلاتا ہے۔

---

## Lesson 1.1 — Creating strings and concatenation

### Concept

A **string** is a sequence of characters: letters, digits, spaces, symbols. In Python, text in quotes is a string.

**Immutability:** We cannot change a string in place. Methods create a **new** string (Lesson 1.2).

### Creating and printing

```python
print("Assalamu Alaikum")
print("Government School Peshawar")
print("Karachi is a big city")
```

### Concatenation

Join strings with `+`. Add `" "` for a space between words.

```python
print("Assalamu" + " " + "Alaikum")
print("Pakistan" + " " + "Zindabad")
print("Class" + " " + "7" + " " + "A")
```

### Urdu / Arabic in strings (same rules)

```python
print("السلام" + " علیکم")
print("مولانا" + " " + "احمد")
```

### Length — `len()`

```python
print(len("Quran"))
print(len("Lahore"))
print(len("Assalamu Alaikum"))
```

`len()` counts every character including spaces.

### Common mistakes

- Forgetting space: `"Hello" + "World"` → `HelloWorld`
- Missing quotes: `print(Hello)` → error

**Practice file:** `1_1_concatenation.py`  
**Checkpoint:** Print full name using 3 strings and `+`; print `len()` of your city name.

---

## Lesson 1.2 — Core string methods

Call a **method** with a dot: `"text".method()`

### Changing case

| Method | Effect |
|--------|--------|
| `.upper()` | ALL CAPS |
| `.lower()` | all small |
| `.title()` | First Letter Of Each Word |
| `.capitalize()` | First letter only |

```python
print("lahore".upper())
print("LaHoRe".lower())
print("assalamu alaikum".title())
print("the holy quran".title())
```

### Removing extra spaces — `.strip()`, `.lstrip()`, `.rstrip()`

```python
print("   Fajr Prayer   ".strip())
print("  Tafsir Ibn Kathir".lstrip())
print("Lahore   ".rstrip())
```

### Replacing text — `.replace(old, new)`

```python
print("Peace be upon you".replace("Peace", "Salam"))
print("I like mango".replace("mango", "cherry"))
```

### Chaining methods

```python
print("  assalamu alaikum  ".strip().title())
```

**Practice file:** `1_2_string_methods.py`  
**Checkpoint:** Take `"  multan  "`, strip and print in uppercase.

---

## Lesson 1.3 — Escape sequences

Inside quotes, special codes:

- `\n` — new line  
- `\t` — tab (space column)

```python
print("Ahmad" + "\t" + "Bilal")
print("Welcome to our class\nSection: 7-A")
```

Formatted list (madrasa or school):

```python
print("Subjects:")
print("\tMathematics")
print("\tScience")
print("\tUrdu")
```

**Practice file:** `1_3_escape_sequences.py`

---

## Lesson 1.4 — Extension (optional)

*Skip in short courses; teach after Module 7 if lists are not yet known.*

### `.split()` and `.join()`

```python
print("Ahmed, Fatima, Hassan".split(", "))
print(" and ".join(["Ahmed", "Fatima", "Hassan"]))
```

### `.startswith()` / `.endswith()`

```python
print("Assalamu Alaikum".startswith("Assalamu"))
print("Lahore".endswith("hore"))
```

### `.find()` and `.count()`

```python
print("Pakistan Zindabad".find("Zindabad"))
print("mississippi".count("s"))
```

**Practice file:** `1_4_extension_methods.py`

---

## Lesson 1.5 — Exercises and quiz

See **ASSESSMENT.md** and files `1_5_quiz.py`, `1_6_solutions.py`.

---

## Exercise sets (summary)

### Set A — Concatenation and len

1. Print "Assalamu Alaikum" using `+` with a space.  
2. Print length of `"Ramadan"`.  
3. Print length of `"Sindh Madressatul Islam"`.  
4. Print `"We are learning Python"` as one string.  
5. Build `"In the name of Allah"` using five strings and `+`.

### Set B — Methods

1. Title-case `"government high school"`.  
2. Uppercase `"jamia ashrafia"`.  
3. Lowercase `"KaRaChI"`.  
4. Strip `"   Eid Mubarak   "`.  
5. Replace `"bus"` with `"van"` in `"I take the bus to school"`.  
6. Chain strip + title on `"  cricket is fun  "`.

### Set C — Escape sequences

1. Two names on one line with tab.  
2. Two lines in one `print` using `\n`.  
3. Heading + three book or subject names with `\t`.

**Full solutions:** `1_6_solutions.py`

---

## Summary and key terms

| Term | Meaning |
|------|---------|
| String | Text in `'...'` or `"..."` |
| Concatenation | Joining with `+` |
| Immutability | Original string unchanged by methods |
| Method | Operation after a dot, e.g. `.upper()` |
| Escape sequence | `\n`, `\t` inside strings |

**Next module:** Variables — store strings and use `input()`.
