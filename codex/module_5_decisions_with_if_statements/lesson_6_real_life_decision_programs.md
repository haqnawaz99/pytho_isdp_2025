# Lesson 6: Real-Life Decision Programs

## Duration

45 minutes

## Learning objective

Students will be able to combine conditions and output to make short, useful decision-based programs.

## Key vocabulary

- decision
- outcome
- program

## Starter

Ask students:

- What real-life decisions can a computer help make?

## Concept explanation

A useful program checks information and then gives a response. In this lesson, students combine input, comparison, and branching in familiar situations.

## Worked example 1

```python
temperature = float(input("Enter temperature: "))

if temperature >= 40:
    print("Stay hydrated and avoid too much sun.")
elif temperature >= 30:
    print("It is a hot day.")
else:
    print("Weather is moderate.")
```

## Worked example 2

```python
runs = int(input("Enter cricket runs: "))

if runs >= 100:
    print("Century")
elif runs >= 50:
    print("Half century")
else:
    print("Keep batting")
```

## Worked example 3

```python
budget = int(input("Enter your budget: "))

if budget >= 1000:
    print("You can buy the full set.")
else:
    print("Choose fewer items.")
```

## Guided practice

Students write a program that asks for marks and prints:

- `Excellent`
- `Pass`
- `Fail`

## Independent practice

### Beginner

Write a weather message program using temperature.

### Intermediate

Write a marks result program using three outcomes.

### Challenge

Write a rainfall or shopping decision program using input and validation.

## Common mistakes

- trying to make the program too complex at once
- wrong ordering of conditions
- weak indentation in multi-branch code

## Assessment checkpoint

1. Why should the highest condition often come first?
2. What concepts are combined in a decision-based program?
3. What makes a program's output useful?

## Exit ticket

Students write one small real-life decision program.

## Homework

Write one complete decision-based program using marks, weather, sports, or budget.
