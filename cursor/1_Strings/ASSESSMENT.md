# Module 1 — Assessment (Strings)

## Learning objectives checklist (teacher)

| # | Objective | Evidence |
|---|-----------|----------|
| 1 | Create strings with quotes | Quiz Q1, Q10 |
| 2 | Concatenate with `+` | Quiz Q1, Q6 |
| 3 | Use `len()` | Quiz Q2, Q10 |
| 4 | Use upper/lower/title/strip/replace | Quiz Q3–Q5, Q9 |
| 5 | Use `\n` and `\t` | Quiz Q6–Q7 |

---

## Multiple choice

1. A string in Python is:
   - a) Text in quotes  
   - b) Only numbers  
   - c) A file name  

2. `"Hello" + "World"` prints:
   - a) HelloWorld  
   - b) Hello World  
   - c) Error always  

3. `len("Lahore")` is:
   - a) 5  
   - b) 6  
   - c) 7  

4. `"  hi  ".strip()` removes:
   - a) Spaces inside hi  
   - b) Leading and trailing spaces  
   - c) All letters  

5. `\n` in a string means:
   - a) New line  
   - b) Number  n  
   - c) No output  

**Answers:** 1-a, 2-a (no space unless added), 3-b (L-a-h-o-r-e = 6), 4-b, 5-a

---

## Short answer

1. What is immutability in one sentence?  
2. When do we use `.title()` instead of `.upper()`?

**Sample:**  
1. Strings do not change in place; methods return new strings.  
2. When each word should start with a capital, not the whole string.

---

## Practical rubric (quiz file)

| Score | Criteria |
|-------|----------|
| 9–10 | All correct, clean code |
| 7–8 | Core Q1–7 correct |
| 5–6 | Concatenation and print OK; methods weak |
| Below 5 | Re-teach Lesson 1.1–1.2 |

---

## Capstone mini-task (end of module)

**Task:** Write `greeting_card.py` (no variables):

- Line 1: Islamic or respectful greeting (concatenation OK)  
- Line 2: Your city in title case from lowercase literal  
- Line 3: Three subjects or books, each on new line with `\t`  
- One comment at top with your name  

**Self-check rubric**

| Done? | Item |
|-------|------|
| [ ] | Runs without error |
| [ ] | Uses `+` at least once |
| [ ] | Uses one method (strip/title/replace) |
| [ ] | Uses `\n` or `\t` |
| [ ] | Has `#` comment |
