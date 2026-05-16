# Lesson 3: Project - Student Report Card

## Duration

45 to 60 minutes

## Learning objective

Students will be able to build a simple report card project using input, conditions, and functions.

## Key vocabulary

- report
- marks
- grade
- result

## Project goal

Create a program that asks for a student's name and marks, then prints a result message.

## Concepts used

- input
- conversion
- `if-elif-else`
- functions
- `return`

## Worked example 1

```python
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 80:
    result = "Excellent"
elif marks >= 50:
    result = "Pass"
else:
    result = "Fail"

print(f"{name}: {result}")
```

## Worked example 2

```python
def grade_message(marks):
    if marks >= 80:
        return "Excellent"
    elif marks >= 50:
        return "Pass"
    else:
        return "Fail"

name = input("Enter student name: ")
marks = int(input("Enter marks: "))
print(f"{name}: {grade_message(marks)}")
```

## Worked example 3

```python
def valid_marks(marks):
    return marks >= 0 and marks <= 100

marks = int(input("Enter marks: "))

if valid_marks(marks):
    print("Marks accepted")
else:
    print("Invalid marks")
```

## Guided build steps

1. Ask for name
2. Ask for marks
3. Validate marks
4. Decide result category
5. Print report line

## Independent practice

### Beginner

Build a report card with pass or fail only.

### Intermediate

Build a report card with three categories.

### Challenge

Add a validation check for marks.

## Common mistakes

- wrong order of grade conditions
- forgetting to convert marks
- not checking invalid marks

## Assessment checkpoint

1. What conditions are needed?
2. Why should marks be validated?
3. What does the grading function return?

## Exit ticket

Students show a working report card output for one sample student.

## Homework

Improve the report card project with one extra useful feature.
