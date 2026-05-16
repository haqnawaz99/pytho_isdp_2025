# Module 3 — Assessment (Data Types)

## Objectives checklist

| # | Objective | Evidence |
|---|-----------|----------|
| 1 | Identify int, float, str, bool | Q1–Q2 |
| 2 | Use type() | Q1–Q2 |
| 3 | int(), float(), str() | Q4–Q5, Q8–Q9 |
| 4 | input + int for math | Q6–Q7 |
| 5 | Explain/fix type errors | Q3, Q10 |

---

## Multiple choice

1. `type(25)` shows:
   - a) `<class 'str'>`  
   - b) `<class 'int'>`  
   - c) `<class 'float'>`  

2. `input("Age? ")` returns:
   - a) int  
   - b) str  
   - c) bool  

3. `int("40") + 10` equals:
   - a) `"4010"`  
   - b) `50`  
   - c) Error always  

4. `int(88.9)` equals:
   - a) `89`  
   - b) `88`  
   - c) `88.9`  

5. `"Marks: " + str(90)` works because:
   - a) str() turns 90 into text  
   - b) 90 is already text  
   - c) + only works on numbers  

**Answers:** 1-b, 2-b, 3-b, 4-b, 5-a

---

## Short answer

1. When do we use `float()` instead of `int()`?  
2. What is the difference between TypeError and ValueError? Give one example of each.

**Sample:**  
1. When the number has a decimal part or user may type `12.5`.  
2. TypeError: wrong types together (str + int). ValueError: conversion impossible (`int("abc")`).

---

## Capstone: `fee_calculator.py`

Program must:

- [ ] Ask student name (str, no conversion needed)  
- [ ] Ask monthly fee in rupees (use `float`)  
- [ ] Ask months (use `int`)  
- [ ] Print total fee (fee × months) using comma or `str`  
- [ ] Print types of two variables using `type()` once  

---

## Rubric (quiz)

| Score | Level |
|-------|--------|
| 9–10 | Ready for Module 4 operators |
| 7–8 | Conversion solid; review errors |
| 5–6 | Re-teach 3.2 with paired practice |
| Below 5 | Repeat Module 2 input + Module 3.1 |

---

## Self-assessment

| I can... | Not yet | Sometimes | Yes |
|----------|---------|-----------|-----|
| Say four data types | | | |
| Use type() | | | |
| int(input(...)) | | | |
| Fix str + int error | | | |
| Use isdigit() before int | | | |
