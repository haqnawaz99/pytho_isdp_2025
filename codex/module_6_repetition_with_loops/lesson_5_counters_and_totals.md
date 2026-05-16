# Lesson 5: Counters and Totals

## Duration

45 minutes

## Learning objective

Students will be able to update a counter or total inside a loop.

## Key vocabulary

- counter
- total
- add
- update

## Starter

Ask students:

- If a student reads 2 pages every day for 5 days, how can we keep adding the total?

## Concept explanation

Inside a loop, we can change a variable again and again. This helps us count events or add totals over time.

## Worked example 1

```python
total = 0

for number in range(1, 6):
    total = total + number

print(total)
```

## Worked example 2

```python
pages_read = 0

for day in range(1, 6):
    pages_read = pages_read + 2

print(pages_read)
```

## Worked example 3

```python
count = 1
total = 0

while count <= 4:
    total = total + 10
    count += 1

print(total)
```

## Guided practice

Students trace:

```python
total = 0

for i in range(3):
    total = total + 5

print(total)
```

## Independent practice

### Beginner

Add numbers from 1 to 4.

### Intermediate

Add 3 rupees daily for 7 days.

### Challenge

Use a `while` loop to add 20 four times.

## Common mistakes

- forgetting to give `total` a starting value
- updating the wrong variable
- printing inside the wrong place when the final total is expected at the end

## Assessment checkpoint

1. What is a counter?
2. What is a running total?
3. Why do we often start totals at 0?

## Exit ticket

Students write one short loop that updates a total.

## Homework

Write a small program that counts or adds something over several days.
