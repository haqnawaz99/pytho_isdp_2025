# Lesson 2: Project - School Canteen Bill

## Duration

45 to 60 minutes

## Learning objective

Students will be able to build a simple bill calculator for a school canteen.

## Key vocabulary

- bill
- total
- quantity
- cost

## Project goal

Create a program that asks for item details and calculates a total bill.

## Concepts used

- variables
- input
- `int()` or `float()`
- arithmetic operators
- `f-strings`
- optional function use

## Worked example 1

```python
item_name = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity
print(f"{item_name} total bill: {total}")
```

## Worked example 2

```python
def calculate_total(price, quantity):
    return price * quantity

item_name = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = calculate_total(price, quantity)
print(f"{item_name} total bill: {total}")
```

## Worked example 3

```python
budget = float(input("Enter budget: "))
total = float(input("Enter total bill: "))

if total <= budget:
    print("Budget is enough.")
else:
    print("Budget is not enough.")
```

## Guided build steps

1. Ask for item name
2. Ask for item price
3. Ask for quantity
4. Calculate total
5. Print the result
6. Optional: compare with budget

## Independent practice

### Beginner

Build a bill for one item only.

### Intermediate

Add a budget check.

### Challenge

Add two items and combine their total.

## Common mistakes

- forgetting to convert price and quantity
- multiplying text instead of numbers
- unclear variable names

## Assessment checkpoint

1. Which inputs are needed?
2. What formula gives the bill?
3. Why do we convert the price and quantity?

## Exit ticket

Students show one working version of the bill calculator.

## Homework

Improve the bill project by adding one extra useful feature.
