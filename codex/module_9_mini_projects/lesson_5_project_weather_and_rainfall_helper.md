# Lesson 5: Project - Weather and Rainfall Helper

## Duration

45 to 60 minutes

## Learning objective

Students will be able to build a local weather helper using numeric input and decision-making.

## Key vocabulary

- temperature
- rainfall
- advice
- condition

## Project goal

Create a program that asks for temperature and rainfall and gives simple advice.

## Concepts used

- input
- `float()`
- `if-elif-else`
- functions
- validation

## Worked example 1

```python
temperature = float(input("Enter temperature: "))

if temperature >= 40:
    print("Very hot day")
elif temperature >= 30:
    print("Hot day")
else:
    print("Moderate weather")
```

## Worked example 2

```python
rainfall = float(input("Enter rainfall: "))

if rainfall > 0:
    print("Rain expected")
else:
    print("Dry weather")
```

## Worked example 3

```python
def weather_advice(temperature, rainfall):
    if temperature >= 40:
        return "Stay hydrated"
    elif rainfall > 0:
        return "Carry an umbrella"
    else:
        return "Weather looks fine"

temperature = float(input("Enter temperature: "))
rainfall = float(input("Enter rainfall: "))

print(weather_advice(temperature, rainfall))
```

## Guided build steps

1. Ask for temperature
2. Ask for rainfall
3. Validate values if needed
4. Decide advice
5. Print the message

## Independent practice

### Beginner

Classify weather using only temperature.

### Intermediate

Use both temperature and rainfall.

### Challenge

Add a validation check for negative rainfall.

## Common mistakes

- forgetting float conversion
- using conditions in the wrong order
- not thinking about invalid rainfall values

## Assessment checkpoint

1. Why is `float()` useful here?
2. Which values should be checked?
3. What makes the output helpful?

## Exit ticket

Students test the project with two different weather conditions.

## Homework

Improve the weather helper with one extra useful message.
