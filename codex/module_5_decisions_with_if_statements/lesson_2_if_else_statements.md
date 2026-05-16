# Lesson 2: `if-else` Statements

## Duration

45 minutes

## Learning objective

Students will be able to use `if-else` to choose between two possible outcomes.

## Key vocabulary

- `else`
- choice
- branch

## Starter

Ask students:

- If a student passes, we show one message. If not, what should happen?

## Concept explanation

An `if-else` statement gives two possible paths. If the condition is true, one block runs. Otherwise, the `else` block runs.

## Worked example 1

```python
marks = 42

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

## Worked example 2

```python
rainfall = 0

if rainfall > 0:
    print("Bring umbrella")
else:
    print("No umbrella needed")
```

## Worked example 3

```python
age = 17

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## Guided practice

Students write:

```python
attendance = 80

if attendance >= 75:
    print("Good attendance")
else:
    print("Improve attendance")
```

## Independent practice

### Beginner

Write a program that checks if a score is above 60.

### Intermediate

Write a program that checks if a temperature is above 35.

### Challenge

Write a program that checks whether a budget is enough for a 500-rupee purchase.

## Common mistakes

- aligning `else` incorrectly
- forgetting that `else` does not need a condition
- expecting both branches to run

## Assessment checkpoint

1. What is the purpose of `else`?
2. How many branches are in an `if-else` statement?
3. Does `else` need a condition?

## Exit ticket

Students write one `if-else` example using weather or marks.

## Homework

Write two `if-else` programs from daily life.
