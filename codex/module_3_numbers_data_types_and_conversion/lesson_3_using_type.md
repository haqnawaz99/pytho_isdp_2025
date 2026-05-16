# Lesson 3: Using `type()`

## Duration

45 minutes

## Learning objective

Students will be able to use `type()` to check what kind of value a variable holds.

## Key vocabulary

- `type()`
- inspect
- data type

## Starter

Ask students:

- How can we check if `25` is text or a number?
- Can Python tell us the type directly?

## Concept explanation

`type()` is a built-in Python function that shows the type of a value or variable. This helps students check their understanding and spot mistakes.

## Worked example 1

```python
print(type("Lahore"))
print(type(25))
```

## Worked example 2

```python
price = 99.5
print(type(price))
```

## Worked example 3

```python
is_student = True
name = "Ayesha"

print(type(is_student))
print(type(name))
```

## Guided practice

Students predict the output type for:

```python
print(type(12.0))
print(type(False))
print(type("12"))
```

## Independent practice

### Beginner

Use `type()` on one string and one integer.

### Intermediate

Use `type()` on four variables with four different data types.

### Challenge

Create values from school or daily life, then check their types.

## Common mistakes

- expecting `type()` to change the value
- confusing the type output with the value itself
- forgetting brackets

## Assessment checkpoint

1. What does `type()` do?
2. What type will Python show for `"25"`?
3. What type will Python show for `25`?

## Exit ticket

Students write one line using `type()`.

## Homework

Write a program that prints the type of:

- your name
- your age
- a price
- a boolean value
