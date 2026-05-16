# Lesson 5: First Introduction to f-Strings

## Duration

45 minutes

## Learning objective

Students will be able to use a simple `f-string` to place variable values inside a message.

## Key vocabulary

- `f-string`
- placeholder
- format

## Starter

Show both:

```python
name = "Ali"
print("Welcome " + name)
```

```python
name = "Ali"
print(f"Welcome {name}")
```

Ask:

- Which one looks easier to read?

## Concept explanation

An `f-string` is a clean way to put variable values into a string. We write `f` before the opening quote, then place the variable name inside curly brackets.

This lesson is only an introduction. Students should use one variable first, then two variables.

## Worked example 1

```python
name = "Zainab"
print(f"Welcome {name}")
```

## Worked example 2

```python
city = "Multan"
print(f"My city is {city}")
```

## Worked example 3

```python
name = input("Enter your name: ")
school = input("Enter your school: ")
print(f"{name} studies at {school}.")
```

## Guided practice

Students write a program that asks for:

- name
- favorite food

Then prints:

- `___ likes ___`

## Independent practice

### Beginner

Use an `f-string` to print your city.

### Intermediate

Ask for a student's name and favorite subject, then print both in one sentence.

### Challenge

Ask for name, city, and school, then print a full introduction using one or two `f-strings`.

## Common mistakes

- forgetting the `f` before the quote
- forgetting curly brackets around the variable
- putting the variable name in plain text instead of inside `{ }`

## Assessment checkpoint

1. What does the `f` mean in an `f-string`?
2. Where do we place the variable name in an `f-string`?
3. Rewrite `print("Hello " + name)` using an `f-string`.

## Exit ticket

Students write one correct `f-string` from memory.

## Homework

Write a program that asks for:

- name
- city
- favorite food

Then print a short introduction using `f-strings`.
