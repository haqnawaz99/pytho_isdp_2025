# Module 0: Getting Started with Python

**Audience:** Mixed madrasa and school students (ages roughly 10–16)  
**Tools:** Laptop, Visual Studio Code, Python 3.10+  
**Code language:** English | **Class language:** Urdu + English mix

---

## Module learning objectives

By the end of this module, students will be able to:

1. Explain what a computer **program** is in simple words.
2. Open the course folder in VS Code and run a `.py` file.
3. Use `print()` to show text on the screen.
4. Add **comments** in code and recognize a simple **syntax error**.

> **Urdu (teacher):** پروگرام وہ ہدایات ہیں جو کمپیوٹر کو بتاتی ہیں کیا کرنا ہے۔ `print` سے ہم اسکرین پر لکھائی دکھاتے ہیں۔

---

## Lesson 0.1 — What is programming?

### Concept

A **program** is a set of instructions written for the computer. We write instructions in a **programming language** — here, **Python**. The computer follows them step by step, very fast and very exactly.

Examples students already understand:

- A **calculator** adds numbers when we press buttons — someone programmed it.
- A **game** moves when we press keys — programmed.
- Our lesson today: a few lines of Python that show messages.

We are not “talking to the computer in Urdu.” We write code in **English words** that Python understands (`print`, `if`, etc.). You explain in Urdu in class; the **code stays in English**.

### Pakistan / madrasa link

Programming can help:

- Keep a list of students in a class (later: lists)
- Calculate total cost of books in rupees (later: variables and math)
- Display a welcome message for a school or Jamia (today: `print`)

### Worked example (discussion only — run in Lesson 0.3)

```python
print("Welcome to Python class")
```

---

## Lesson 0.2 — VS Code and your first folder

See **SETUP_VS_CODE.md** in the parent `cursor` folder.

**Class routine (every lesson):**

1. Open VS Code → Open Folder → `cursor`
2. Open the lesson file from the left panel
3. Save (Ctrl+S)
4. Run (play button or F5)

> **Urdu:** فائل محفوظ کریں، پھر Run دبائیں۔

---

## Lesson 0.3 — The `print()` function

### Concept

`print()` **displays** whatever we put inside the parentheses. Text must be in **quotes** `"like this"` — that text is a **string** (Module 1 goes deeper).

### Example 1 — Simple messages

```python
print("Hello Students")
print("Assalamu Alaikum")
print("We are learning Python")
```

- Each line is one instruction. Python runs from **top to bottom**.

### Example 2 — School and city (Pakistan context)

```python
print("Government High School Multan")
print("I love cricket")
print("Pakistan Zindabad")
```

### Example 3 — Madrasa context

```python
print("Jamia Ashrafia Lahore")
print("Seeking knowledge is important")
print("Surah Al-Fatiha")
```

### Practice (hands-on)

Write a program that prints **four** lines about yourself: name, city, favourite subject, one hobby.

### Common mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| `Print("hi")` | Capital P — Python is case-sensitive | Use `print` |
| `print(hi)` | Missing quotes | `print("hi")` |
| `print "hi"` | Old Python 2 style | Use `print("hi")` |

### Checkpoint

Student runs a file that prints at least 3 lines without copying from the board.

---

## Lesson 0.4 — Comments and errors

### Concept — Comments

A **comment** is a note for humans. Python **ignores** it.

```python
# This is a comment - Python skips this line
print("This line runs")  # comment at end of line
```

> **Urdu:** `#` کے بعد لکھا سب نوٹ ہے، کمپیوٹر نہیں چلاتا۔

### Example — Organizing your code

```python
# Greeting section
print("Assalamu Alaikum")

# School section
print("Class 7 - Section A")
```

### Concept — Errors

If we break Python’s rules, we get an **error message** in red in the Terminal. Read the **last line** — it often says `SyntaxError` (typing mistake) or `NameError` (wrong name).

**Example of SyntaxError:**

```python
print("Hello"   # forgot closing quote and parenthesis
```

**Fix:** Count quotes and brackets: every `(` needs `)`, every `"` needs a closing `"`.

### Checkpoint

1. Student adds two comments to their own program.
2. Teacher shows one broken line; student identifies the fix.

---

## Summary

| Term | Meaning |
|------|---------|
| Program | Instructions for the computer |
| Python | The language we learn |
| `print()` | Shows output on the screen |
| String | Text in quotes `"..."` |
| Comment | Line starting with `#` — not executed |
| Syntax error | Grammar mistake in code |

**Next module:** Strings — joining text, changing case, formatting lines.
