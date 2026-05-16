# Lesson 1: Basic `if` Statements

## Duration

45 minutes

## Learning objective

Students will be able to write a simple `if` statement that runs only when a condition is true.

## Key vocabulary

- `if`
- condition
- true

## Starter

Ask students:

- If marks are above 50, what should the program say?
- Should the message appear for every student?

## Concept explanation

An `if` statement checks a condition. If the condition is true, Python runs the indented block below it.

Basic pattern:

```python
if condition:
    do_something
```

## Worked example 1

```python
marks = 85

if marks >= 50:
    print("Pass")
```

## Worked example 2

```python
temperature = 38

if temperature >= 35:
    print("It is a very hot day.")
```

## Worked example 3

```python
runs = 54

if runs >= 50:
    print("Half century")
```

## Guided practice

Students predict the output:

```python
age = 12

if age >= 10:
    print("You can join the coding club.")
```

## Independent practice

### Beginner

Write a program that prints `Good score` if marks are 70 or higher.

### Intermediate

Write a program that prints `Warm weather` if temperature is above 30.

### Challenge

Write a program that prints `Big score` if cricket runs are more than 80.

## Common mistakes

- forgetting the colon `:`
- not indenting the print line
- using `=` instead of `==` or another comparison operator

## Assessment checkpoint

1. What does an `if` statement do?
2. When does the indented block run?
3. What is wrong with `if marks = 50:`?

## Exit ticket

Students write one working `if` statement from memory.

## Homework

Write three small `if` examples using marks, age, or weather.
