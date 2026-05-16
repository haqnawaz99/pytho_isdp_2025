# Lesson 4: Looping Through Lists

## Duration

45 minutes

## Learning objective

Students will be able to use a loop to process all items in a list.

## Key vocabulary

- loop
- item
- each

## Starter

Ask students:

- If a list has five items, do we want five separate `print()` lines?

## Concept explanation

We can use a `for` loop to go through each item in a list one by one.

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
    print(f"I like {food}")
```

## Worked example 3

```python
subjects = ["Math", "Urdu", "Science"]

for subject in subjects:
    print(f"Study {subject}")
```

## Guided practice

Students write a list of three sports or hobbies and print each using a loop.

## Independent practice

### Beginner

Print each fruit in a fruit list.

### Intermediate

Print each city with a message.

### Challenge

Print each shopping item with numbering or a simple sentence.

## Common mistakes

- forgetting the colon
- using the list name instead of the item variable inside the loop
- bad indentation

## Assessment checkpoint

1. What does `for city in cities:` mean?
2. Why are loops useful with lists?
3. What gets printed in each repetition?

## Exit ticket

Students write one loop over a list.

## Homework

Create two lists and use loops to print all items.
