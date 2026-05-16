# Lesson 5: Simple Validation

## Duration

45 minutes

## Learning objective

Students will be able to check whether user input is acceptable using simple conditions.

## Key vocabulary

- validate
- valid
- invalid
- check

## Starter

Ask students:

- If someone enters marks above 100, should a school result program accept that?

## Concept explanation

Validation means checking whether input is acceptable before using it.

Simple examples:

- marks should be between 0 and 100
- age should not be negative
- class section should not be empty

## Worked example 1

```python
marks = int(input("Enter marks: "))

if marks >= 0 and marks <= 100:
    print("Valid marks")
else:
    print("Invalid marks")
```

## Worked example 2

```python
age = int(input("Enter age: "))

if age >= 0:
    print("Valid age")
else:
    print("Invalid age")
```

## Worked example 3

```python
rainfall = float(input("Enter rainfall: "))

if rainfall >= 0:
    print("Valid rainfall value")
else:
    print("Invalid rainfall value")
```

## Guided practice

Students write a program that checks whether attendance is between 0 and 100.

## Independent practice

### Beginner

Check whether a number is positive.

### Intermediate

Check whether marks are between 0 and 100.

### Challenge

Check whether a budget entered by the user is at least 0.

## Common mistakes

- forgetting both sides of a range check
- using text input without conversion
- assuming every input is valid

## Assessment checkpoint

1. What is validation?
2. Why should marks above 100 be rejected?
3. What operator is useful in range checks?

## Exit ticket

Students write one validation condition.

## Homework

Write two validation examples from school or home life.
