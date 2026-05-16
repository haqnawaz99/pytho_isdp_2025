# Lesson 6: Common Conversion Mistakes

## Duration

40 to 45 minutes

## Learning objective

Students will be able to identify common conversion errors and explain how to fix them.

## Key vocabulary

- error
- invalid
- convert
- debug

## Starter

Show students:

```python
age = int("12.5")
```

Ask:

- Will this work?
- Why or why not?

## Concept explanation

Some conversions work, and some do not. Students should learn to notice why a value is invalid for a certain conversion.

Examples:

- `int("15")` works
- `int("15.5")` does not work
- `float("15.5")` works
- `int("Ali")` does not work

## Worked example 1

```python
number = int("25")
print(number)
```

## Worked example 2

```python
price = float("75.5")
print(price)
```

## Worked example 3

```python
name = "Ali"
# int(name) would cause an error because "Ali" is not a number
print(name)
```

## Guided practice

Ask students which of these will work:

- `int("50")`
- `float("7.25")`
- `int("Hello")`
- `int("3.5")`

## Independent practice

### Beginner

Mark each as valid or invalid:

- `int("9")`
- `float("2.2")`
- `int("City")`

### Intermediate

Explain why `int("5.5")` fails.

### Challenge

Fix the following:

```python
price = int("12.75")
```

## Common mistakes

- using `int()` for decimal text
- trying to convert names into numbers
- not reading the data carefully before conversion

## Assessment checkpoint

1. Why does `int("12.5")` fail?
2. Which conversion should we use for `"12.5"`?
3. Can we use `int()` on `"Lahore"`?

## Exit ticket

Students write one valid and one invalid conversion example.

## Homework

Write three valid conversions and explain each in one short line.
