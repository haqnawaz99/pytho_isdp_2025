# Module 8 Quiz: Lists and Collections

## Part A: Multiple Choice

1. Which symbol pair is used for a list?
   - A. `( )`
   - B. `[ ]`
   - C. `{ }`
   - Answer: B

2. What is the first index of a list?
   - A. 1
   - B. 0
   - C. -1
   - Answer: B

3. What does `.append()` do?
   - A. removes an item
   - B. adds an item to the list
   - C. compares items
   - Answer: B

4. What happens to duplicates in a set?
   - A. they are kept
   - B. they are sorted
   - C. they are removed
   - Answer: C

5. A dictionary stores data as:
   - A. positions only
   - B. key-value pairs
   - C. repeated loops
   - Answer: B

## Part B: Short Answer

1. What is a list?
2. Why does indexing start at 0 matter?
3. What is one difference between a list and a tuple?
4. What is one difference between a list and a set?
5. What is a key in a dictionary?

## Part C: Coding

1. Create a list of three cities and print the second item.
2. Create a list of two foods and append one more.
3. Create a dictionary of two subjects and their marks, then print one mark.

## Answer Key

### Part B Suggested Answers

1. A list stores multiple items in one collection.
2. It helps us access the correct item by position.
3. A list can change, while a tuple is generally fixed.
4. A set stores only unique items.
5. A key is the name used to access a value in a dictionary.

### Part C Suggested Solutions

```python
cities = ["Lahore", "Karachi", "Multan"]
print(cities[1])
```

```python
foods = ["Biryani", "Samosa"]
foods.append("Mango")
print(foods)
```

```python
marks = {"Math": 85, "Urdu": 78}
print(marks["Math"])
```
