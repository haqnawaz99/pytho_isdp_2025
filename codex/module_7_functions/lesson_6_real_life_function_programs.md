# Lesson 6: Real-Life Function Programs

## Duration

45 minutes

## Learning objective

Students will be able to organize a short real-life program into functions.

## Key vocabulary

- organize
- reuse
- function

## Starter

Ask students:

- Which parts of a school result program could be made into separate functions?

## Concept explanation

Functions make longer programs easier to read and manage. Instead of one long block of code, we can split work into small named parts.

## Worked example 1

```python
def show_welcome(name):
    print(f"Welcome {name}")

def show_city(city):
    print(f"City: {city}")

show_welcome("Ayesha")
show_city("Lahore")
```

## Worked example 2

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(120, 4)
print(f"Total cost: {total}")
```

## Worked example 3

```python
def grade_message(marks):
    if marks >= 80:
        return "Excellent"
    elif marks >= 50:
        return "Pass"
    else:
        return "Fail"

print(grade_message(72))
```

## Guided practice

Students write a program with:

- one greeting function
- one calculation function

## Independent practice

### Beginner

Write a function that prints a study message and call it twice.

### Intermediate

Write a function that returns total cost from price and quantity.

### Challenge

Write a small marks or weather program using two functions.

## Common mistakes

- putting too much code into one function
- forgetting to call the function
- mixing return-based and print-based thinking

## Assessment checkpoint

1. Why do functions make programs better?
2. When should a function return a value?
3. How can two small functions help organize one program?

## Exit ticket

Students write one short real-life function example.

## Homework

Write a complete program that uses at least two functions.
