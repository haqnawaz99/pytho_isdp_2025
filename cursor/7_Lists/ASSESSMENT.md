# Module 7 — Assessment (Lists & Dictionaries)

## Objectives checklist

| # | Objective | Evidence |
|---|-----------|----------|
| 1 | List create, index, len | Q1–Q2 |
| 2 | append, remove, sort | Q3–Q4 |
| 3 | for on list | Q5 |
| 4 | Tuple basics | Q6 |
| 5 | Dict access, update | Q7–Q9 |
| 6 | List of dicts | Q10 |

---

## Multiple choice

1. First item of `items` is:
   - a) `items[1]`  
   - b) `items[0]`  
   - c) `items[-0]`  

2. `.append(x)`:
   - a) adds x to end of list  
   - b) removes x  
   - c) sorts list  

3. In `student = {"name": "Ali"}`, access name with:
   - a) `student["name"]`  
   - b) `student(0)`  
   - c) `name.student`  

4. Tuple is:
   - a) mutable like list  
   - b) immutable  
   - c) key-value pairs  

5. `{"a", "b", "a"}` as set has how many items?
   - a) 3  
   - b) 2  
   - c) 1  

**Answers:** 1-b, 2-a, 3-a, 4-b, 5-b

---

## Short answer

1. When use a list vs a dictionary?  
2. What does `pupil["marks"]` mean if `pupil` is a dictionary?

**Sample:**  
1. List for ordered collection; dict when each item has a label/name.  
2. Value stored under key `"marks"`.

---

## Capstone: `class_register.py`

- [ ] List of at least 3 student dicts (`name`, `marks`, `city`)  
- [ ] Loop: print each student on one line (f-string)  
- [ ] Count and print how many passed (`marks >= 50`)  
- [ ] Dict `school_info` with `name`, `city`, `subjects` (list) — print all subjects in a loop  
- [ ] One list method: `append` a new student  

---

## Rubric

| Score | Level |
|-------|--------|
| 9–10 | Ready for Module 8 projects |
| 7–8 | Dict or index weak |
| 5–6 | Re-teach 7.1–7.2 |
| Below 5 | Review loops + variables |

---

## Self-assessment

| I can... | Not yet | Sometimes | Yes |
|----------|---------|-----------|-----|
| Use index 0 and -1 | | | |
| append and sort | | | |
| Make and use a dict | | | |
| Loop list of dicts | | | |
