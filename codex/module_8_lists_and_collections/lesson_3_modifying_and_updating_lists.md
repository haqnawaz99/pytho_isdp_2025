# Lesson 3: Modifying and Updating Lists

## Duration

45 minutes

## Learning objective

Students will be able to add, change, and remove items in a list.

## Key vocabulary

- append
- update
- remove

## Starter

Ask students:

- What if you want to add one more fruit to your list?
- What if one item was written incorrectly?

## Concept explanation

Lists are changeable. We can:

- add an item with `.append()`
- change an item by index
- remove an item with `.remove()`

## Worked example 1

```python
fruits = ["Mango", "Banana"]
fruits.append("Apple")
print(fruits)
```

## Worked example 2

```python
cities = ["Lahore", "Karachi", "Multan"]
cities[1] = "Islamabad"
print(cities)
```

## Worked example 3

```python
subjects = ["Math", "Urdu", "Science"]
subjects.remove("Urdu")
print(subjects)
```

## Guided practice

Students write a list of three foods, then:

- add one item
- change one item

## Independent practice

### Beginner

Append one city to a city list.

### Intermediate

Change one subject in a subject list.

### Challenge

Remove one shopping item from a shopping list.

## Common mistakes

- forgetting brackets in `.append()` or `.remove()`
- changing the wrong index
- removing an item that is not in the list

## Assessment checkpoint

1. What does `.append()` do?
2. How do we change an item at a certain position?
3. What does `.remove()` do?

## Exit ticket

Students update one list in two different ways.

## Homework

Write a short program that creates a list and then changes it.
