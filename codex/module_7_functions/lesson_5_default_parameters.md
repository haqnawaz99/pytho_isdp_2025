# Lesson 5: Default Parameters

## Duration

45 minutes

## Learning objective

Students will be able to use a simple default parameter in a function.

## Key vocabulary

- default
- optional
- parameter

## Starter

Ask students:

- What if a greeting should normally say `Student` unless we give a different name?

## Concept explanation

A default parameter gives a function a ready-made value. If we do not pass a different value, Python uses the default.

## Worked example 1

```python
def greet(name="Student"):
    print(f"Welcome {name}")

greet()
greet("Ali")
```

## Worked example 2

```python
def show_city(city="Lahore"):
    print(f"City: {city}")

show_city()
show_city("Peshawar")
```

## Worked example 3

```python
def study_message(subject="Python"):
    print(f"Today we study {subject}")

study_message()
study_message("Science")
```

## Guided practice

Students write a function with one default parameter for a food name.

## Independent practice

### Beginner

Write a function with a default name.

### Intermediate

Write a function with a default city.

### Challenge

Write a function with a default subject and call it with and without a new value.

## Common mistakes

- thinking the default always replaces passed values
- forgetting brackets during the call
- making examples too complex too early

## Assessment checkpoint

1. What is a default parameter?
2. When is the default value used?
3. What happens if we pass a new value?

## Exit ticket

Students write one function with a default parameter.

## Homework

Write two functions that use default values in a simple way.
