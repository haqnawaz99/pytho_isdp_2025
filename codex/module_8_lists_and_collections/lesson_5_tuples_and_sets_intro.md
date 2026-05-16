# Lesson 5: Introduction to Tuples and Sets

## Duration

45 minutes

## Learning objective

Students will be able to explain the basic idea of tuples and sets and how they differ from lists.

## Key vocabulary

- tuple
- set
- duplicate

## Starter

Ask students:

- What if a collection should not change?
- What if we want only unique items?

## Concept explanation

Python has other collection types besides lists.

- A tuple is like a list, but it is not meant to change.
- A set stores unique items and removes duplicates.

This lesson is only an introduction.

## Worked example 1

```python
weekdays = ("Mon", "Tue", "Wed")
print(weekdays)
```

## Worked example 2

```python
fruits = {"Mango", "Banana", "Mango"}
print(fruits)
```

Teacher note:

- Explain that the duplicate `Mango` appears only once in the set.

## Worked example 3

```python
list_example = ["A", "B", "A"]
set_example = {"A", "B", "A"}

print(list_example)
print(set_example)
```

## Guided practice

Students compare:

- a list with repeated values
- a set with repeated values

## Independent practice

### Beginner

Create one tuple of three cities.

### Intermediate

Create one set of fruits with one repeated item.

### Challenge

Explain one difference between a list and a tuple, and one difference between a list and a set.

## Common mistakes

- expecting sets to keep duplicates
- expecting tuples to be changed like lists
- thinking sets keep a fixed visible order like lists

## Assessment checkpoint

1. What is a tuple?
2. What is a set?
3. What happens to duplicates in a set?

## Exit ticket

Students give one example of a tuple or set.

## Homework

Write one list, one tuple, and one set. Explain each in one short line.
