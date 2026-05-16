# Lesson 4: Functions with Return Values

## Duration

45 minutes

## Learning objective

Students will be able to use `return` to send a result back from a function.

## Key vocabulary

- return
- result
- value

## Starter

Ask students:

- What if we want a function to calculate something and give us the answer back?

## Concept explanation

Some functions print a message. Other functions return a value so the program can use it later.

Important difference:

- `print()` shows output
- `return` sends a value back

## Worked example 1

```python
def add_two_numbers(a, b):
    return a + b

result = add_two_numbers(4, 5)
print(result)
```

## Worked example 2

```python
def get_full_greeting(name):
    return f"Assalamu Alaikum {name}"

message = get_full_greeting("Amina")
print(message)
```

## Worked example 3

```python
def square(number):
    return number * number

print(square(6))
```

## Guided practice

Students write a function that returns double a number.

## Independent practice

### Beginner

Write a function that returns `10`.

### Intermediate

Write a function that returns the sum of two numbers.

### Challenge

Write a function that returns a sentence using a name parameter.

## Common mistakes

- printing when a returned value is needed
- forgetting the `return` keyword
- not storing or using the returned value

## Assessment checkpoint

1. What is the difference between `print()` and `return`?
2. What does a returned value allow us to do?
3. In what kind of function is `return` useful?

## Exit ticket

Students write one function that returns a value.

## Homework

Write two functions that return values and print the returned results.
