# Lesson 5: Logical Operators

## Duration

45 minutes

## Learning objective

Students will be able to explain and use `and`, `or`, and `not` in simple boolean expressions.

## Key vocabulary

- logical operator
- condition
- and
- or
- not

## Starter

Ask students:

- If both homework and attendance are complete, what word can join those two ideas?
- If tea or milk is available, what word joins those options?

## Concept explanation

Logical operators work with boolean values and comparisons.

- `and` is true when both sides are true
- `or` is true when at least one side is true
- `not` changes true to false, or false to true

## Worked example 1

```python
print(True and True)
print(True and False)
```

## Worked example 2

```python
marks = 70
attendance = 90

print((marks >= 50) and (attendance >= 75))
```

## Worked example 3

```python
is_hot = True
print(not is_hot)

print((5 > 2) or (3 > 7))
```

## Guided practice

Students predict:

```python
print((10 > 5) and (8 == 8))
print((4 > 9) or (7 < 10))
print(not (6 == 6))
```

## Independent practice

### Beginner

Write one `and` example using `True` and `False`.

### Intermediate

Use `marks` and `attendance` variables and write one logical expression.

### Challenge

Create two comparisons joined by `or`, then explain the result.

## Common mistakes

- reading `and` and `or` too quickly without checking both sides
- forgetting brackets around comparisons
- confusing `not` with negative numbers

## Assessment checkpoint

1. When is `and` true?
2. When is `or` true?
3. What does `not` do?

## Exit ticket

Students write one logical expression using a comparison.

## Homework

Write three logical operator examples and explain each result.
