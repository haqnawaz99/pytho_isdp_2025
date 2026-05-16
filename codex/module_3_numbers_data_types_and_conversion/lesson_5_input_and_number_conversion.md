# Lesson 5: Input and Number Conversion

## Duration

45 minutes

## Learning objective

Students will be able to convert user input into numbers before using it in a simple program.

## Key vocabulary

- input
- convert
- integer
- float

## Starter

Ask students:

- If a student types `15`, does Python receive a number or text?

## Concept explanation

`input()` returns text. If the user types a number and we want to treat it like a number later, we should convert it.

Important pattern:

```python
age = int(input("Enter your age: "))
```

## Worked example 1

```python
age = int(input("Enter your age: "))
print(age)
print(type(age))
```

## Worked example 2

```python
temperature = float(input("Enter temperature: "))
print(temperature)
print(type(temperature))
```

## Worked example 3

```python
marks = int(input("Enter your marks: "))
print(f"Your marks are {marks}.")
```

## Guided practice

Students write a program that asks for:

- age
- cricket runs

Then prints both.

## Independent practice

### Beginner

Ask the user for age and print it.

### Intermediate

Ask the user for a notebook price with decimal and print it.

### Challenge

Ask the user for marks and temperature and print both with `f-strings`.

## Common mistakes

- forgetting that `input()` alone returns text
- using `int()` on decimal text
- converting after the wrong step

## Assessment checkpoint

1. What type does `input()` return before conversion?
2. When should we use `int(input(...))`?
3. When should we use `float(input(...))`?

## Exit ticket

Students write one line that asks for a decimal number and stores it correctly.

## Homework

Write a program that asks the user for:

- age
- price

Then print both values.
