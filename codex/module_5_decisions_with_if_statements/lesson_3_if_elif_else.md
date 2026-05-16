# Lesson 3: `if-elif-else`

## Duration

45 minutes

## Learning objective

Students will be able to use `if-elif-else` when a program needs more than two possible outcomes.

## Key vocabulary

- `elif`
- multiple choices
- category

## Starter

Ask students:

- If marks can be excellent, good, or needs improvement, is `if-else` enough?

## Concept explanation

`elif` means "else if". It lets a program check another condition if the first one is false.

## Worked example 1

```python
marks = 78

if marks >= 80:
    print("Excellent")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")
```

## Worked example 2

```python
temperature = 39

if temperature >= 40:
    print("Extreme heat")
elif temperature >= 30:
    print("Hot day")
else:
    print("Pleasant weather")
```

## Worked example 3

```python
runs = 95

if runs >= 100:
    print("Century")
elif runs >= 50:
    print("Half century")
else:
    print("Below fifty")
```

## Guided practice

Students predict:

```python
rain = 25

if rain > 40:
    print("Heavy rain")
elif rain > 10:
    print("Medium rain")
else:
    print("Low rain")
```

## Independent practice

### Beginner

Classify marks into pass or fail with one `elif`.

### Intermediate

Classify a student's attendance as excellent, acceptable, or weak.

### Challenge

Classify a shopping budget as low, medium, or high.

## Common mistakes

- putting conditions in the wrong order
- forgetting that Python checks from top to bottom
- writing too many unrelated branches in one lesson

## Assessment checkpoint

1. What does `elif` mean?
2. Why does order matter in `if-elif-else`?
3. How many branches can an `if-elif-else` structure have?

## Exit ticket

Students write one 3-outcome conditional example.

## Homework

Write a program that classifies temperature, marks, or rainfall into three categories.
