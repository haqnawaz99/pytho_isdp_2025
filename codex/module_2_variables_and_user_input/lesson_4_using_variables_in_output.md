# Lesson 4: Using Variables in Output

## Duration

45 minutes

## Learning objective

Students will be able to combine stored values with fixed text in output messages.

## Key vocabulary

- output
- message
- concatenate

## Starter

Show students:

```python
name = "Hamza"
print("Welcome " + name)
```

Ask:

- What part stays fixed?
- What part can change?

## Concept explanation

Variables become more useful when we use them inside bigger messages. We can join fixed text and variable values together to print meaningful output.

## Worked example 1

```python
name = "Amina"
print("Welcome " + name)
```

## Worked example 2

```python
city = "Karachi"
print("My city is " + city)
```

## Worked example 3

```python
student_name = input("Enter your name: ")
print("Assalamu Alaikum " + student_name)
```

## Guided practice

Students write:

```python
school_name = input("Enter your school name: ")
print("You study at " + school_name)
```

## Independent practice

### Beginner

Ask for a name and print `Hello ___`.

### Intermediate

Ask for a favorite subject and print `You like ___`.

### Challenge

Ask for name, city, and favorite food, then print one line for each.

## Common mistakes

- forgetting a space in the fixed string
- printing the variable name in quotes instead of the value
- using the wrong variable in the message

## Assessment checkpoint

1. What is the difference between `print(name)` and `print("name")`?
2. Why do we put a space in `"Welcome "`?
3. Write one line that prints `My city is Lahore` using a variable.

## Exit ticket

Students create one personalized greeting using input and output.

## Homework

Write a short program that asks for a student's name and class, then prints two welcome lines.
