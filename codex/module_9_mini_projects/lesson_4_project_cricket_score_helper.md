# Lesson 4: Project - Cricket Score Helper

## Duration

45 to 60 minutes

## Learning objective

Students will be able to build a cricket score helper using conditions and functions.

## Key vocabulary

- runs
- score
- innings
- milestone

## Project goal

Create a program that reads cricket runs and gives a milestone message.

## Concepts used

- input
- `int()`
- `if-elif-else`
- functions
- optional loops for repeated messages

## Worked example 1

```python
runs = int(input("Enter runs: "))

if runs >= 100:
    print("Century")
elif runs >= 50:
    print("Half century")
else:
    print("Below fifty")
```

## Worked example 2

```python
def score_message(runs):
    if runs >= 100:
        return "Century"
    elif runs >= 50:
        return "Half century"
    else:
        return "Below fifty"

runs = int(input("Enter runs: "))
print(score_message(runs))
```

## Worked example 3

```python
player = input("Enter player name: ")
runs = int(input("Enter runs: "))

print(f"{player}: {runs} runs")
```

## Guided build steps

1. Ask for player name
2. Ask for runs
3. Decide milestone message
4. Print the result

## Independent practice

### Beginner

Create a score helper without player name.

### Intermediate

Add player name and milestone message.

### Challenge

Add another category such as `Duck` for 0 runs.

## Common mistakes

- wrong order of conditions
- forgetting to convert runs
- writing milestone labels that do not match the condition logic

## Assessment checkpoint

1. Why must the century condition come before half century?
2. What input is needed?
3. What is the function's job in this project?

## Exit ticket

Students run the program with two different score values.

## Homework

Add one more feature to the cricket helper project.
