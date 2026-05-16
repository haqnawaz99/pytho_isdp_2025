# Lesson 4: Comparing User Input

## Duration

45 minutes

## Learning objective

Students will be able to compare user input in conditions and produce different messages.

## Key vocabulary

- input
- compare
- response

## Starter

Ask students:

- How can a program ask a user a question and react to the answer?

## Concept explanation

We can store input from the user and then compare it inside an `if` statement.

For text answers:

```python
answer = input("Enter yes or no: ")
```

For number answers:

```python
marks = int(input("Enter marks: "))
```

## Worked example 1

```python
answer = input("Did you complete homework? (yes/no): ")

if answer == "yes":
    print("Well done")
else:
    print("Please complete it soon")
```

## Worked example 2

```python
marks = int(input("Enter your marks: "))

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

## Worked example 3

```python
city = input("Enter your city: ")

if city == "Lahore":
    print("You entered Lahore.")
else:
    print("You entered another city.")
```

## Guided practice

Students write a program that asks for rainfall and prints:

- `Rainy day` if rainfall is above 0
- `Dry day` otherwise

## Independent practice

### Beginner

Ask the user for age and print `Teenager` if age is 13 or more.

### Intermediate

Ask the user for runs and print `Half century` if runs are 50 or more.

### Challenge

Ask the user for temperature and classify it into two or three categories.

## Common mistakes

- forgetting to convert numeric input
- comparing text input with the wrong spelling or case
- using `=` inside the condition

## Assessment checkpoint

1. Why do we use `int(input(...))` for marks?
2. What kind of input can we compare as text?
3. What happens if the condition is false?

## Exit ticket

Students write one input-based `if-else` example.

## Homework

Write a small program that asks the user one question and gives two different answers.
