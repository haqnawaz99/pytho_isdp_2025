# Lesson 6: Operator Precedence

## Duration

45 minutes

## Learning objective

Students will be able to predict the order of operations in Python and use brackets to make expressions clear.

## Key vocabulary

- precedence
- order
- bracket
- expression

## Starter

Show:

```python
print(10 + 5 * 2)
```

Ask:

- Does Python add first or multiply first?

## Concept explanation

Python follows an order of operations similar to BODMAS:

1. brackets
2. powers
3. multiply, divide, floor division, modulus
4. add and subtract

Brackets make code easier to understand and reduce mistakes.

## Worked example 1

```python
print(10 + 5 * 2)
print((10 + 5) * 2)
```

## Worked example 2

```python
print(2 ** 3 + 4)
print((2 + 3) * 4)
```

## Worked example 3

```python
budget = 2000
book_total = 3 * 250
snacks = 150
left = budget - (book_total + snacks)

print(left)
```

## Guided practice

Students predict:

```python
print(6 + 2 * 3)
print((6 + 2) * 3)
print(20 - 8 / 2)
```

## Independent practice

### Beginner

Find the result of:

- `5 + 3 * 2`
- `(5 + 3) * 2`

### Intermediate

Write one expression where brackets change the answer.

### Challenge

Create a short budget program using brackets clearly.

## Common mistakes

- calculating left to right without checking precedence
- forgetting that brackets change the result
- writing long expressions without clarity

## Assessment checkpoint

1. Which happens first in `10 + 4 * 2`?
2. Why are brackets useful?
3. What is the result of `(8 + 2) * 3`?

## Exit ticket

Students write one pair of expressions where brackets create different results.

## Homework

Write three expressions and explain the order in which Python solves them.
