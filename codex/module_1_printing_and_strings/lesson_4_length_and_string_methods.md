# Lesson 4: Length and Simple String Methods

## Duration

45 minutes

## Learning objective

Students will be able to count characters using `len()` and improve text using simple string methods.

## Key vocabulary

- length
- method
- uppercase
- lowercase
- strip

## Starter

Ask students:

- Which is longer: `Lahore` or `Islamabad`?
- How can Python count letters for us?

## Concept explanation

The function `len()` counts the number of characters in a string. Python also gives us string methods that help change or clean text.

Methods for this lesson:

- `.upper()`
- `.lower()`
- `.title()`
- `.strip()`

## Worked example 1

```python
print(len("Lahore"))
print(len("Pakistan"))
```

Teacher note:

- Explain that spaces also count as characters.

## Worked example 2

```python
print("eid mubarak".title())
print("lahore".upper())
print("KARACHI".lower())
```

## Worked example 3

```python
print("  Multan  ".strip())
print(len("Class 7"))
```

## Guided practice

Students predict the output of:

```python
print("python".upper())
print("  mango  ".strip())
print(len("my city"))
```

## Independent practice

### Beginner

Use `len()` on your name.

### Intermediate

Write one line that changes `pakistan` to title case.

### Challenge

Clean this string and print its length:

```python
"  Hyderabad  "
```

## Common mistakes

- thinking `len()` counts words instead of characters
- forgetting brackets in method calls
- expecting `.strip()` to remove spaces from the middle of text

## Assessment checkpoint

1. What does `len()` return?
2. What does `.upper()` do?
3. What does `.strip()` remove?

## Exit ticket

Students write one example using `len()` and one example using a string method.

## Homework

Write a short program that:

- prints your city in uppercase
- prints your school name in title case
- prints the length of your favorite food name
