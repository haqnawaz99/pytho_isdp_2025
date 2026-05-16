# Module 5 Quiz: Decisions with If Statements

## Part A: Multiple Choice

1. What does an `if` statement do?
   - A. repeats code
   - B. makes a decision
   - C. creates a list
   - Answer: B

2. Which symbol is correct for equality comparison?
   - A. `=`
   - B. `==`
   - C. `:=`
   - Answer: B

3. What does `else` do?
   - A. checks another condition
   - B. stores a variable
   - C. runs when the `if` condition is false
   - Answer: C

4. What does `elif` mean?
   - A. end loop if
   - B. else if
   - C. equal if
   - Answer: B

5. Why is indentation important in Python?
   - A. it changes the code block structure
   - B. it makes text colorful
   - C. it changes variable names
   - Answer: A

## Part B: Short Answer

1. What is a condition?
2. What is the difference between `if-else` and `if-elif-else`?
3. Why do we often convert marks input to `int`?
4. What is validation?

## Part C: Coding

1. Write a program that prints `Pass` if marks are 50 or more.
2. Write a program that asks for temperature and prints `Hot` if it is 35 or more, otherwise `Not hot`.
3. Write a program that checks whether attendance is between 0 and 100.

## Answer Key

### Part B Suggested Answers

1. A condition is a true/false check used to make a decision.
2. `if-else` has two outcomes, while `if-elif-else` can handle more than two.
3. Because `input()` returns text and marks should be treated as a number.
4. Validation means checking whether input is acceptable.

### Part C Suggested Solutions

```python
marks = 70

if marks >= 50:
    print("Pass")
```

```python
temperature = float(input("Enter temperature: "))

if temperature >= 35:
    print("Hot")
else:
    print("Not hot")
```

```python
attendance = int(input("Enter attendance: "))

if attendance >= 0 and attendance <= 100:
    print("Valid attendance")
else:
    print("Invalid attendance")
```
