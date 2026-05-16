# Lesson 6: Real-Life Loop Programs

## Duration

45 minutes

## Learning objective

Students will be able to create short real-life programs using loops.

## Key vocabulary

- repeat
- daily
- total
- track

## Starter

Ask students:

- What tasks in school, sports, or home life happen again and again?

## Concept explanation

Loops become useful when we apply repetition to everyday situations. This lesson combines loops with variables, input, and simple calculations.

## Worked example 1

```python
pages_per_day = 2

for day in range(1, 6):
    print(f"Day {day}: read {pages_per_day} pages")
```

## Worked example 2

```python
expense = 100
total = 0

for day in range(1, 6):
    total = total + expense

print(f"Total weekly expense: {total}")
```

## Worked example 3

```python
over = 1

while over <= 3:
    print(f"Over {over}: keep batting carefully")
    over += 1
```

## Guided practice

Students write a program for:

- revising one topic each day for 4 days

## Independent practice

### Beginner

Write a loop that prints a homework reminder 5 times.

### Intermediate

Write a program that counts total pages read in a week.

### Challenge

Write a loop-based sports, shopping, or study tracker.

## Common mistakes

- choosing the wrong kind of loop
- forgetting to update the `while` loop variable
- mixing up loop repetition with one-time code

## Assessment checkpoint

1. When is a `for` loop a good choice?
2. When is a `while` loop a good choice?
3. What makes a loop-based program useful?

## Exit ticket

Students write one short real-life loop program.

## Homework

Write one complete loop program using a school, home, sports, or weather context.
