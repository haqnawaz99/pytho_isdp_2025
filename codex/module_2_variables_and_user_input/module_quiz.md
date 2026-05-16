# Module 2 Quiz: Variables and User Input

## Part A: Multiple Choice

1. What is a variable?
   - A. a type of bracket
   - B. a named place to store a value
   - C. a print command
   - Answer: B

2. What does `=` do in Python?
   - A. compares two values
   - B. stores a value in a variable
   - C. joins two strings
   - Answer: B

3. Which is a valid variable name?
   - A. `my city`
   - B. `2name`
   - C. `student_name`
   - Answer: C

4. What does `input()` do?
   - A. shows a diagram
   - B. asks the user for information
   - C. converts text to numbers
   - Answer: B

5. Which is an `f-string`?
   - A. `print("Hello name")`
   - B. `print(f"Hello {name}")`
   - C. `print(name f"Hello")`
   - Answer: B

## Part B: Short Answer

1. What is the difference between `name` and `"name"`?
2. Why do we store the result of `input()` in a variable?
3. What makes a variable name meaningful?
4. What are curly brackets used for in an `f-string`?

## Part C: Coding

1. Create a variable called `city` and store `Lahore`.
2. Ask the user for their favorite fruit and print it.
3. Write an `f-string` that prints `Ayesha studies at City School.`

## Answer Key

### Part B Suggested Answers

1. `name` is a variable name, while `"name"` is a string.
2. We store it so we can use the user's answer later in the program.
3. It should clearly describe what value is stored.
4. They hold the variable name inside the `f-string`.

### Part C Suggested Solutions

```python
city = "Lahore"
```

```python
favorite_fruit = input("Enter your favorite fruit: ")
print(favorite_fruit)
```

```python
name = "Ayesha"
school = "City School"
print(f"{name} studies at {school}.")
```
