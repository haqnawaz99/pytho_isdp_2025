# Lesson 3: `for` Loops with Items

## Duration

45 minutes

## Learning objective

Students will be able to use a `for` loop to go through simple items such as names, foods, or cities.

## Key vocabulary

- item
- list
- each

## Starter

Show:

```python
cities = ["Lahore", "Karachi", "Multan"]
```

Ask:

- How can we print each city without writing three separate `print()` lines?

## Concept explanation

A `for` loop can go through each item in a collection one by one.

This lesson only introduces the idea lightly. The full topic of lists will come later.

## Worked example 1

```python
cities = ["Lahore", "Karachi", "Multan"]

for city in cities:
    print(city)
```

## Worked example 2

```python
foods = ["Biryani", "Samosa", "Mango"]

for food in foods:
    print(food)
```

## Worked example 3

```python
subjects = ["Math", "Science", "Urdu"]

for subject in subjects:
    print(f"I study {subject}")
```

## Guided practice

Students write a loop for:

- three favorite games

## Independent practice

### Beginner

Print each item in a list of three fruits.

### Intermediate

Print each subject in a list of school subjects.

### Challenge

Print each city in a list with the message `I want to visit ___`.

## Common mistakes

- forgetting the colon
- using the collection name instead of the loop item name
- thinking the whole list is printed one item at a time automatically without a loop

## Assessment checkpoint

1. What does `for city in cities:` mean?
2. What happens inside the loop block?
3. Does the loop process one item or all items at once?

## Exit ticket

Students write one `for` loop over items.

## Homework

Write one loop for foods and one loop for cities.
