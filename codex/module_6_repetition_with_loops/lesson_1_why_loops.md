# Lesson 1: Why Loops?

## Duration

40 minutes

## Learning objective

Students will be able to explain why loops are useful in programming.

## Key vocabulary

- loop
- repeat
- again

## Starter

Write this on the board:

```python
print("Study time")
print("Study time")
print("Study time")
print("Study time")
print("Study time")
```

Ask:

- Is there a shorter way to do this?

## Concept explanation

A loop repeats code. Instead of writing the same instruction many times, we can ask Python to repeat it for us.

## Worked example 1

```python
for number in range(5):
    print("Study time")
```

Teacher note:

- Do not fully explain `range()` yet. Focus on the idea of repetition first.

## Worked example 2

```python
for number in range(3):
    print("Revision")
```

## Worked example 3

```python
for number in range(4):
    print("Practice Python")
```

## Guided practice

Ask students which is better:

- five repeated `print()` lines
- one loop

## Independent practice

### Beginner

Write a loop that prints `Hello` three times.

### Intermediate

Write a loop that prints `Keep learning` four times.

### Challenge

Write a loop that prints your city name five times.

## Common mistakes

- forgetting the colon
- not indenting the print line
- thinking `number` must be printed even if it is not used

## Assessment checkpoint

1. Why do we use loops?
2. What does a loop help us avoid?
3. What part of the code is repeated?

## Exit ticket

Students explain in one sentence why loops are useful.

## Homework

Write two short examples where a loop is better than repeating the same print line.
