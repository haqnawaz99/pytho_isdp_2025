# Lesson 3: Functions with Parameters

## Duration

45 minutes

## Learning objective

Students will be able to pass values into a function using parameters.

## Key vocabulary

- parameter
- argument
- input

## Starter

Ask students:

- What if we want the same greeting function to work for different names?

## Concept explanation

A parameter is a named input for a function. It allows the same function to work with different values.

## Worked example 1

```python
def greet(name):
    print(f"Welcome {name}")

greet("Ali")
greet("Ayesha")
```

## Worked example 2

```python
def show_city(city):
    print(f"My city is {city}")

show_city("Karachi")
show_city("Multan")
```

## Worked example 3

```python
def show_marks(student, marks):
    print(f"{student} scored {marks}")

show_marks("Hamza", 85)
```

## Guided practice

Students write a function that takes one food name and prints a message.

## Independent practice

### Beginner

Write a function that takes one name and prints `Hello ___`.

### Intermediate

Write a function that takes one city and prints a message.

### Challenge

Write a function with two parameters: subject and marks.

## Common mistakes

- forgetting to pass an argument during the call
- confusing the parameter name with a fixed value
- using quotes around a numeric argument when not needed

## Assessment checkpoint

1. What is a parameter?
2. What is an argument?
3. Why are parameters useful?

## Exit ticket

Students write one function with one parameter.

## Homework

Write two functions with parameters based on school, city, or food examples.
