# Lesson 3: User Input

## Duration

45 minutes

## Learning objective

Students will be able to use `input()` to ask the user for text and store the answer in a variable.

## Key vocabulary

- input
- prompt
- user

## Starter

Ask students:

- How can a program ask a question?
- What information might a school program ask from a student?

## Concept explanation

`input()` allows Python to ask the user for information. The text inside `input()` is called the prompt. Whatever the user types is returned as text, and we usually store it in a variable.

## Worked example 1

```python
name = input("Enter your name: ")
print(name)
```

## Worked example 2

```python
city = input("Enter your city: ")
print(city)
```

## Worked example 3

```python
favorite_food = input("What is your favorite food? ")
print(favorite_food)
```

## Guided practice

Students write a program that asks for:

- name
- city

Then prints both answers on separate lines.

## Independent practice

### Beginner

Ask the user for their favorite fruit and print it.

### Intermediate

Ask the user for their school name and print it.

### Challenge

Ask the user for their favorite subject and favorite city, then print both.

## Common mistakes

- writing `input("Enter your name: ")` without storing the result
- confusing the prompt text with the user's answer
- forgetting that the answer is stored as text

## Assessment checkpoint

1. What does `input()` do?
2. What is a prompt?
3. Where should we usually store the result of `input()`?

## Exit ticket

Students write one line of code that asks for a user's city.

## Homework

Write a program that asks the user for:

- their name
- their school or madrasa
- their favorite food
