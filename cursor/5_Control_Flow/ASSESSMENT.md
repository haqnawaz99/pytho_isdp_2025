# Module 5 — Assessment (Control Flow)

## Objectives checklist

| # | Objective | Evidence |
|---|-----------|----------|
| 1 | if + indent | Q1, Q4 |
| 2 | if/else | Q2, Q9 |
| 3 | elif chain | Q3, Q9 |
| 4 | and in condition | Q4, Q5 |
| 5 | while + += | Q6 |
| 6 | for, range, list | Q7, Q8, Q10 |

---

## Multiple choice

1. After `if x > 5:` the next line must be:
   - a) Indented  
   - b) In capitals  
   - c) On the same line always  

2. `else` runs when:
   - a) The if condition is False  
   - b) Always  
   - c) The if condition is True  

3. `range(1, 4)` produces:
   - a) 1, 2, 3  
   - b) 1, 2, 3, 4  
   - c) 0, 1, 2, 3  

4. `while count <= 5` needs inside the loop:
   - a) count changing toward stopping  
   - b) only print  
   - c) import  

5. `elif` is checked when:
   - a) All previous if/elif were False  
   - b) Always after else  
   - c) Never with else  

**Answers:** 1-a, 2-a, 3-a, 4-a, 5-a

---

## Short answer

1. What is the difference between `if` and `while`?  
2. When do we use `elif` instead of many separate `if`?

**Sample:**  
1. `if` runs once if true; `while` repeats while true.  
2. When only one branch should run (grades, menu choices).

---

## Capstone: `attendance_checker.py`

- [ ] Ask total students and absent (int)  
- [ ] if/else: print “Class full” if absent == 0 else print present count  
- [ ] Ask marks; elif chain for A/B/C/D/F (same bands as lesson)  
- [ ] for loop over list `["Homework", "Test", "Project"]` printing each  
- [ ] while loop printing 1..3 with `Bismillah` or step message  

---

## Rubric

| Score | Level |
|-------|--------|
| 9–10 | Ready for functions |
| 7–8 | Fix indent / elif order |
| 5–6 | Re-teach if/else only |
| Below 5 | Review Module 4 comparisons |

---

## Self-assessment

| I can... | Not yet | Sometimes | Yes |
|----------|---------|-----------|-----|
| Write if with colon and indent | | | |
| Use else and elif | | | |
| Write while with += | | | |
| Use for and range() | | | |
| Loop over a list | | | |
