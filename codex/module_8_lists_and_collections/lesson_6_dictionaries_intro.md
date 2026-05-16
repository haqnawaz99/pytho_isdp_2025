# Lesson 6: Introduction to Dictionaries

## Duration

45 minutes

## Learning objective

Students will be able to create a simple dictionary and use keys to get values.

## Key vocabulary

- dictionary
- key
- value

## Starter

Ask students:

- What if we want to store a subject together with its marks?

## Concept explanation

A dictionary stores information as key-value pairs.

Examples:

- subject -> marks
- city -> population label
- prayer -> time

## Worked example 1

```python
marks = {"Math": 85, "Urdu": 78, "Science": 90}
print(marks)
```

## Worked example 2

```python
prayer_times = {"Fajr": "5:00", "Maghrib": "6:45"}
print(prayer_times["Fajr"])
```

## Worked example 3

```python
student = {"name": "Ali", "city": "Lahore"}
print(student["name"])
print(student["city"])
```

## Guided practice

Students create a dictionary of two subjects and their marks.

## Independent practice

### Beginner

Create a dictionary with two cities and labels.

### Intermediate

Create a dictionary with two school subjects and marks.

### Challenge

Create a dictionary for a student with name, class, and city.

## Common mistakes

- using indexes instead of keys
- forgetting curly brackets
- trying to access a key that does not exist

## Assessment checkpoint

1. What is a dictionary?
2. What is a key?
3. How do we access a value from a dictionary?

## Exit ticket

Students write one simple dictionary and read one value.

## Homework

Write two dictionaries from daily life and access one value from each.
