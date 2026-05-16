# Lesson 4: `while` Loops

## Duration

45 minutes

## Learning objective

Students will be able to use a `while` loop with a stopping condition.

## Key vocabulary

- `while`
- condition
- stop

## Starter

Ask students:

- If we want to keep counting until we reach 5, what should tell the loop to stop?

## Concept explanation

A `while` loop keeps running while its condition is true. It needs a condition and usually needs an update to avoid running forever.

## Worked example 1

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## Worked example 2

```python
pages = 1

while pages <= 3:
    print("Revise one page")
    pages += 1
```

## Worked example 3

```python
tries = 1

while tries <= 4:
    print("Try again")
    tries += 1
```

## Guided practice

Students trace:

```python
number = 2

while number <= 4:
    print(number)
    number += 1
```

## Independent practice

### Beginner

Print numbers from 1 to 3 using `while`.

### Intermediate

Print a message 5 times using `while`.

### Challenge

Write a `while` loop that counts from 2 to 10 by 2.

## Common mistakes

- forgetting to update the loop variable
- creating an infinite loop
- wrong indentation

## Assessment checkpoint

1. When does a `while` loop stop?
2. Why do we update the counter?
3. What happens if we forget `count += 1`?

## Exit ticket

Students write a working `while` loop with a counter.

## Homework

Write two `while` loops: one for counting, one for repeating a message.
