# Lesson 4: Type Conversion

## Duration

45 minutes

## Learning objective

Students will be able to convert between strings and numbers using `int()`, `float()`, and `str()`.

## Key vocabulary

- convert
- `int()`
- `float()`
- `str()`

## Starter

Show:

- `"25"`
- `25`

Ask:

- They look similar. Are they the same in Python?
- How can we change one into the other?

## Concept explanation

Type conversion changes a value from one type to another.

Important beginner conversions:

- `int("25")` gives `25`
- `float("25.5")` gives `25.5`
- `str(25)` gives `"25"`

## Worked example 1

```python
marks_text = "90"
marks_number = int(marks_text)

print(marks_number)
print(type(marks_number))
```

## Worked example 2

```python
temperature_text = "36.5"
temperature_number = float(temperature_text)

print(temperature_number)
print(type(temperature_number))
```

## Worked example 3

```python
age = 14
age_text = str(age)

print(age_text)
print(type(age_text))
```

## Guided practice

Students convert:

- `"100"` to integer
- `"5.75"` to float
- `45` to string

## Independent practice

### Beginner

Convert `"12"` to an integer.

### Intermediate

Convert `"250.50"` to a float.

### Challenge

Convert a number into a string and place it inside a sentence.

## Common mistakes

- trying `int("12.5")`
- expecting `str()` to keep the value as a number
- forgetting to store the converted result

## Assessment checkpoint

1. What does `int()` do?
2. What does `float()` do?
3. Why do we use `str()`?

## Exit ticket

Students write one example of conversion from string to integer.

## Homework

Write one example each using:

- `int()`
- `float()`
- `str()`
