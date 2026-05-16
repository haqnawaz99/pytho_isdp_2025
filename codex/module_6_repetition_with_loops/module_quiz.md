# Module 6 Quiz: Repetition with Loops

## Part A: Multiple Choice

1. Why do we use loops?
   - A. to stop Python
   - B. to repeat code
   - C. to make strings
   - Answer: B

2. What does `range(5)` produce in a `for` loop?
   - A. 1, 2, 3, 4, 5
   - B. 0, 1, 2, 3, 4
   - C. only 5
   - Answer: B

3. Which loop continues while a condition is true?
   - A. `for`
   - B. `if`
   - C. `while`
   - Answer: C

4. What is a common cause of an infinite loop?
   - A. using `print()`
   - B. forgetting to update the counter
   - C. using a variable
   - Answer: B

5. Why do we often start a total at 0?
   - A. because totals grow from nothing
   - B. because 0 is a string
   - C. because loops require it only once
   - Answer: A

## Part B: Short Answer

1. What is a loop?
2. What is the difference between a `for` loop and a `while` loop?
3. Why is indentation important in loops?
4. What is a counter?

## Part C: Coding

1. Write a `for` loop that prints numbers from 1 to 5.
2. Write a `while` loop that prints `Hello` three times.
3. Write a loop that adds 5 four times and prints the total.

## Answer Key

### Part B Suggested Answers

1. A loop repeats code.
2. A `for` loop is often used for a known number of repetitions, while a `while` loop runs while a condition is true.
3. Indentation shows which code belongs inside the loop.
4. A counter is a variable that changes step by step, often to track repetitions.

### Part C Suggested Solutions

```python
for number in range(1, 6):
    print(number)
```

```python
count = 1

while count <= 3:
    print("Hello")
    count += 1
```

```python
total = 0

for i in range(4):
    total = total + 5

print(total)
```
