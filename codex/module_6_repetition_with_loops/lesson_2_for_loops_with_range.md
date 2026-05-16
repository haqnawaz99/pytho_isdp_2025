# Lesson 2: `for` Loops with `range()`

## Duration

45 minutes

## Learning objective

Students will be able to use `for` loops with `range()` to repeat code a known number of times.

## Key vocabulary

- `for`
- `range()`
- count

## Starter

Ask students:

- If we want to print numbers from 1 to 5, how can Python help?

## Concept explanation

A `for` loop can run a block of code a fixed number of times. `range()` creates a counting sequence.

Useful beginner patterns:

- `range(5)` gives 0, 1, 2, 3, 4
- `range(1, 6)` gives 1, 2, 3, 4, 5

## Worked example 1

```python
for number in range(5):
    print(number)
```

## Worked example 2

```python
for number in range(1, 6):
    print(number)
```

## Worked example 3

```python
for day in range(1, 8):
    print(f"Day {day}: revise 2 pages")
```

## Guided practice

Students predict:

```python
for i in range(2, 6):
    print(i)
```

## Independent practice

### Beginner

Print numbers from 1 to 5.

### Intermediate

Print numbers from 1 to 10.

### Challenge

Print `Practice` 6 times using a `for` loop.

## Common mistakes

- expecting `range(5)` to start at 1
- forgetting the end value is not included
- poor indentation inside the loop

## Assessment checkpoint

1. What does `range(5)` produce?
2. What does `range(1, 6)` produce?
3. How many times does the loop run in `range(3)`?

## Exit ticket

Students write one `for` loop with `range()`.

## Homework

Write a loop that prints numbers from 1 to 8 and another that prints a message 4 times.
