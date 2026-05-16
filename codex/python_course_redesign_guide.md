# Redesigned Python Course Guide for Pakistani School and Madrasa Learners

## Table of Contents

1. Course Review Summary
2. Design Principles
3. Recommended Audience and Delivery Model
4. Detailed Curriculum Map
5. Standard Lesson Structure
6. Pakistan-Specific Content Enhancements
7. Sample Complete Lesson Units
8. Code Examples and Practice Bank
9. Assessment Strategy
10. Resource Recommendations
11. Teacher Guidance Notes
12. Action Items for Course Implementation

---

## 1. Course Review Summary

### Overall judgment

The existing course has a strong intention, a clear desire to teach step by step, and useful effort toward local relevance. However, it needs significant redesign in structure, consistency, lesson pacing, and classroom usability.

### Strengths to preserve

- Localized examples already exist and should be retained where they are simple and meaningful.
- The early written chapter style is more suitable for teachers than the later large print-heavy scripts.
- The course includes quizzes and solutions, which is valuable for guided learning.
- Core Python concepts are mostly technically correct and use modern syntax.

### Content that needs significant revision

- `Variables` currently overlaps with `Data Types`, `Operators`, and `Formatting`.
- Later modules become too long and too dense for beginners.
- Some lessons introduce several new ideas at the same time.
- A number of files include broken character encoding and emoji-heavy formatting that reduce professionalism and readability.
- The course uses mostly Islamic-only examples in later lessons. That should be broadened to include mainstream Pakistani student life while keeping Islamic sensitivity.

### Review across the requested dimensions

#### 1. Content Structure and Progression

- The sequence is partially logical but not consistently scaffolded.
- Topic duplication creates confusion about what belongs where.
- Reinforcement exists, but it is not strategically planned.
- Advanced topics appear too early in some later lessons.

#### 2. Age and Cultural Appropriateness

- The course is respectful and relevant to Pakistani learners.
- Examples are often culturally familiar, especially for Madrasa contexts.
- The language is sometimes too text-heavy for younger bilingual learners.
- Islamic framing is appropriate in many places, but the course needs broader school-friendly examples too.

#### 3. Engagement and Examples

- There are many examples, but not enough variety in task type.
- Students need more mini-projects, pair exercises, prediction tasks, and debugging tasks.
- Real-life local problems can be used more effectively.

#### 4. Technical Accuracy

- The material appears broadly correct for modern Python.
- `f-strings` are used, which is good.
- Python course documentation should explicitly target Python 3.11 or newer.
- Some pedagogical choices are weak even where syntax is correct, such as combining too many ideas in one lesson.

#### 5. Learning Outcomes

- Learning goals are inconsistent.
- Checkpoints are present in spirit but not standardized.
- Measurable outcomes should be added to every lesson and module.

---

## 2. Design Principles

This redesign uses the following principles:

- One lesson, one main idea.
- Simple language first, proper terminology second.
- Use English for code and core terms, with Urdu support where helpful.
- Balance school life, family life, Pakistani culture, and Islamic respect.
- Move from concrete to abstract.
- Use short examples before full programs.
- Build frequent low-stakes practice into every lesson.
- Teach debugging and mistake-checking from the beginning.

---

## 3. Recommended Audience and Delivery Model

### Target audience

- Mixed beginner learners roughly ages 11 to 16
- Pakistani school students
- Madrasa and Jamia students beginning programming
- English-medium or Urdu-medium learners with partial English comfort

### Recommended language model

- Main explanation in simple English
- Short Urdu support words where useful
- Examples:
  - variable = "naam rakhne wala dabba"
  - loop = "dobarah chalne wala hissa"
  - condition = "shart"

### Recommended delivery format

- Teacher-facing markdown lesson notes
- Short runnable `.py` examples per lesson
- Printable exercises and quizzes
- Optional notebook version later, after the written curriculum is stabilized

---

## 4. Detailed Curriculum Map

### Module 0: Digital Readiness and Python Setup

- Duration: 2 lessons, 35-45 minutes each
- Learning objectives:
  - Open Python or an offline editor
  - Run a simple script
  - Understand what a program is
- Key concepts:
  - Python as a language
  - Running code
  - Output using `print()`
- Build toward:
  - Confidence with the environment before syntax-heavy lessons

### Module 1: Printing and Strings

- Duration: 4 lessons
- Learning objectives:
  - Print text correctly
  - Understand strings as text data
  - Use quotes, spaces, and simple string methods
- Key concepts:
  - `print()`
  - string literals
  - concatenation
  - `len()`
  - `.upper()`, `.lower()`, `.title()`, `.strip()`
- Build toward:
  - Using strings later with variables and input

### Module 2: Variables and User Input

- Duration: 4 lessons
- Learning objectives:
  - Store values in variables
  - Choose sensible variable names
  - Take input from the user
  - Combine stored values in output
- Key concepts:
  - assignment
  - naming rules
  - `input()`
  - simple message building
  - first use of `f-strings`
- Build toward:
  - using variables in conditions and calculations

### Module 3: Numbers, Data Types, and Conversion

- Duration: 4 lessons
- Learning objectives:
  - Distinguish `int`, `float`, `str`, and `bool`
  - Convert input into numbers when needed
  - Avoid string-number mistakes
- Key concepts:
  - `type()`
  - `int()`, `float()`, `str()`
  - Boolean values
- Build toward:
  - numeric programs and decision making

### Module 4: Operators and Calculations

- Duration: 4 lessons
- Learning objectives:
  - Use arithmetic operators
  - Understand comparison operators
  - Apply logical operators in simple conditions
  - Read expressions using precedence
- Key concepts:
  - `+`, `-`, `*`, `/`, `//`, `%`, `**`
  - `==`, `!=`, `>`, `<`, `>=`, `<=`
  - `and`, `or`, `not`
  - precedence with brackets
- Build toward:
  - `if` statements and real-world calculations

### Module 5: Decisions with If Statements

- Duration: 5 lessons
- Learning objectives:
  - Make programs choose between actions
  - Use `if`, `elif`, and `else`
  - Write clear condition-based logic
- Key concepts:
  - conditional flow
  - nested decisions
  - simple validation
- Build toward:
  - interactive programs

### Module 6: Repetition with Loops

- Duration: 5 lessons
- Learning objectives:
  - Repeat actions with `for` and `while`
  - Count with `range()`
  - Stop infinite loops
- Key concepts:
  - `for`
  - `while`
  - counters
  - accumulation
- Build toward:
  - list processing and small games

### Module 7: Functions

- Duration: 5 lessons
- Learning objectives:
  - Define and call functions
  - Use parameters and return values
  - Break large problems into smaller parts
- Key concepts:
  - `def`
  - parameters
  - return values
  - default parameters
- Build toward:
  - reusable project code

### Module 8: Lists and Collections

- Duration: 6 lessons
- Learning objectives:
  - Store multiple values in a list
  - Access and modify list items
  - Iterate through collections
  - Get introduced to tuples, sets, and dictionaries at the right pace
- Key concepts:
  - lists
  - indexing
  - append, remove, sort
  - tuples
  - sets
  - dictionaries
- Build toward:
  - record keeping and simple data projects

### Module 9: Mini Projects

- Duration: 4 to 6 lessons
- Learning objectives:
  - Combine multiple concepts in realistic programs
  - Debug and improve existing code
  - Present a completed project
- Suggested projects:
  - school canteen bill calculator
  - prayer timetable organizer using sample data
  - cricket score helper
  - weather and crop advice starter tool
  - student result report

---

## 5. Standard Lesson Structure

Every lesson should use this structure:

1. Starter review, 5 minutes
2. Learning objective, 2 minutes
3. Concept explanation, 8-10 minutes
4. Teacher-led worked examples, 10-12 minutes
5. Guided practice, 8-10 minutes
6. Independent practice, 10-15 minutes
7. Common mistakes discussion, 3-5 minutes
8. Exit ticket or checkpoint, 3-5 minutes

### Lesson template

- Learning objective:
  - Students will be able to...
- Key vocabulary:
  - 3 to 5 words only
- Concept explanation:
  - short, concrete, no long theory block
- Worked examples:
  - 2 or 3 examples
- Practice:
  - beginner, medium, challenge
- Common mistakes:
  - show and fix
- Assessment:
  - 2 quick questions or 1 small coding task

---

## 6. Pakistan-Specific Content Enhancements

### Example contexts to use throughout

- Cities: Lahore, Karachi, Peshawar, Quetta, Multan, Hyderabad, Islamabad
- Schools and Madaris: attendance, marks, homework, hifz progress, library books
- Food: biryani, samosa, roti, mangoes, dates, lassi
- Sports: cricket score, football goals, kabaddi team points
- Family life: Eid shopping, bus fare, electricity units, guest lists
- Agriculture: rainfall, crop count, wheat bags, milk production
- Weather: hot day alerts, monsoon rainfall, temperature logs

### Urdu support terms

- variable: "naam wala box"
- input: "user se maloomat lena"
- output: "screen par nateeja"
- condition: "shart"
- loop: "dobarah chalna"
- function: "kaam karne wala block"

### Cultural guidance

- Use Islamic examples where natural, not forced.
- Avoid sectarian or sensitive religious debate content.
- Use respectful names for boys and girls.
- Balance Madrasa, government school, and private school contexts.
- Prefer practical examples over moralizing examples.

---

## 7. Sample Complete Lesson Units

## Lesson Unit 1: Printing and Strings

### Lesson title

Printing Messages in Python

### Duration

40 minutes

### Learning objective

Students will be able to print text, identify a string, and join simple strings to make a message.

### Key vocabulary

- `print()`
- string
- quotes
- concatenate

### Concept explanation

A string is text inside quotes. Python prints text using `print()`. If we want to join text pieces together, we can use `+`. Students should first see strings as messages they already know: names, city names, greetings, and class labels.

### Worked example 1

```python
print("Assalamu Alaikum")
print("Welcome to Python class")
```

Explanation:

- The text inside quotes is a string.
- `print()` shows that string on the screen.

### Worked example 2

```python
print("Lahore")
print("Karachi")
print("Peshawar")
```

Explanation:

- Each line prints one city name.
- This helps students see that strings can be one word or many words.

### Worked example 3

```python
print("Eid" + " " + "Mubarak")
print("Class" + " " + "7")
```

Explanation:

- `+` joins strings together.
- `" "` is a string containing one space.

### Guided practice

Ask students to write code that prints:

- their name
- their school or madrasa name
- their favorite food

### Independent practice

#### Beginner

Print these exactly:

- `Pakistan Zindabad`
- `Python is fun`

#### Intermediate

Join these into one output line:

- `Cricket`
- `Match`
- `Today`

#### Challenge

Print:

- `My city is Multan`

using at least two joined strings.

### Common mistakes to watch for

- forgetting quotes around text
- missing a closing quote
- forgetting spaces when joining strings

### Assessment checkpoint

1. What is a string?
2. What does `print()` do?
3. Write one line of code to print `Hello Pakistan`.

### Short practice solutions

```python
print("Pakistan Zindabad")
print("Python is fun")
print("Cricket" + " " + "Match" + " " + "Today")
print("My city is " + "Multan")
```

### Teacher notes

- Let students predict the output before running code.
- Ask them what happens if quotes are removed.
- Keep this lesson very concrete.

---

## Lesson Unit 2: Variables and Input

### Lesson title

Saving Information in Variables

### Duration

45 minutes

### Learning objective

Students will be able to store text in variables, take user input, and print personalized messages.

### Key vocabulary

- variable
- assignment
- input
- value

### Concept explanation

A variable is a named place that stores a value. A simple Urdu support explanation is: variable ek naam wala box hai. Students should see that variables help avoid repeating the same text again and again.

### Worked example 1

```python
name = "Ayesha"
print(name)
```

Explanation:

- `name` is the variable.
- `"Ayesha"` is the value stored in it.

### Worked example 2

```python
city = "Quetta"
print("My city is " + city)
```

Explanation:

- The variable can be used inside a bigger message.

### Worked example 3

```python
student_name = input("Enter your name: ")
print("Welcome, " + student_name)
```

Explanation:

- `input()` takes data from the user.
- The typed answer is stored in `student_name`.

### Guided practice

Students write a program that asks for:

- name
- class
- favorite subject

Then prints a welcome message.

### Independent practice

#### Beginner

Store your favorite fruit in a variable and print it.

#### Intermediate

Ask the user for their city and print:

`You live in ___`

#### Challenge

Ask for name and school, then print one complete sentence using both.

### Common mistakes to watch for

- writing `name "Ali"` instead of `name = "Ali"`
- forgetting that `input()` returns text
- confusing variable names with string values

### Assessment checkpoint

1. What is a variable?
2. What does the `=` sign do in Python?
3. Write a program that asks for a student's name and prints it.

### Practice solutions

```python
fruit = "Mango"
print(fruit)
```

```python
city = input("Enter your city: ")
print("You live in " + city)
```

```python
name = input("Enter your name: ")
school = input("Enter your school: ")
print(f"{name} studies at {school}.")
```

### Teacher notes

- Show the difference between `name` and `"name"`.
- Encourage meaningful variable names.
- Introduce `f-strings` only after students are comfortable with simple concatenation.

---

## Lesson Unit 3: If Statements

### Lesson title

Making Decisions with `if`

### Duration

45 minutes

### Learning objective

Students will be able to use `if`, `elif`, and `else` to make simple decisions in a Python program.

### Key vocabulary

- condition
- true
- false
- `if`
- `else`

### Concept explanation

Programs do not always do the same thing. Sometimes they make a decision based on a condition. In Urdu support language, this can be explained as a "shart". If the condition is true, one block runs. Otherwise another block can run.

### Worked example 1

```python
marks = 85

if marks >= 50:
    print("Pass")
```

Explanation:

- The condition is `marks >= 50`.
- Because 85 is greater than 50, Python prints `Pass`.

### Worked example 2

```python
temperature = 38

if temperature >= 35:
    print("It is a very hot day.")
else:
    print("Weather is moderate.")
```

Explanation:

- Only one branch runs.
- This is a familiar Pakistan weather example.

### Worked example 3

```python
day = input("Enter day type (school/holiday): ")

if day == "school":
    print("Pack your bag.")
elif day == "holiday":
    print("Enjoy your rest and reading time.")
else:
    print("Please enter school or holiday.")
```

Explanation:

- `if` checks the first condition.
- `elif` checks another condition if needed.
- `else` handles everything not matched earlier.

### Guided practice

Students create a simple fee checker:

- if amount is 0: print `No fee due`
- if amount is less than 1000: print `Small balance`
- otherwise: print `Large balance`

### Independent practice

#### Beginner

Check if a number is greater than 10.

#### Intermediate

Ask the user for cricket runs and print `Half century` if runs are 50 or more.

#### Challenge

Ask the user for rainfall in mm:

- less than 10: `Low rain`
- 10 to 40: `Medium rain`
- above 40: `Heavy rain`

### Common mistakes to watch for

- forgetting the colon `:`
- bad indentation
- using `=` instead of `==`
- making conditions too complicated too early

### Assessment checkpoint

1. What does an `if` statement do?
2. What is the difference between `=` and `==`?
3. Write a program that prints `Bring umbrella` if rain is greater than 0.

### Practice solutions

```python
number = 14

if number > 10:
    print("Greater than 10")
```

```python
runs = int(input("Enter runs: "))

if runs >= 50:
    print("Half century")
```

```python
rain = int(input("Enter rainfall in mm: "))

if rain < 10:
    print("Low rain")
elif rain <= 40:
    print("Medium rain")
else:
    print("Heavy rain")
```

### Teacher notes

- Use board tracing: write the condition, then ask students whether it is true or false.
- Have students physically point to which branch will run.
- Spend time on indentation because this is the first big syntax hurdle.

---

## 8. Code Examples and Practice Bank

This section gives extra topic-wise examples beyond the sample lessons.

### Major Topic: Strings

#### Example 1

```python
print("My favorite fruit is mango.")
```

#### Example 2

```python
message = "eid mubarak"
print(message.title())
```

#### Example 3

```python
city = " Lahore "
print(city.strip())
```

#### Example 4

```python
print(len("Pakistan"))
```

#### Practice exercises

1. Print your full name.
2. Print the length of your school name.
3. Clean the text `"  Multan  "` using a string method.

#### Solutions

```python
print("Muhammad Hamza")
```

```python
print(len("City School"))
```

```python
print("  Multan  ".strip())
```

### Major Topic: Numbers and Conversion

#### Example 1

```python
age = 13
print(type(age))
```

#### Example 2

```python
price = 99.5
print(type(price))
```

#### Example 3

```python
marks = input("Enter marks: ")
marks = int(marks)
print(marks + 5)
```

#### Example 4

```python
weight = "42.5"
print(float(weight))
```

#### Practice exercises

1. Ask the user for age and add 1.
2. Convert `"250"` to an integer.
3. Convert `45` to a string and print it with a message.

#### Solutions

```python
age = int(input("Enter age: "))
print(age + 1)
```

```python
number = int("250")
print(number)
```

```python
count = 45
print("Total students: " + str(count))
```

### Major Topic: Operators

#### Example 1

```python
print(8 + 5)
```

#### Example 2

```python
print(20 // 3)
print(20 % 3)
```

#### Example 3

```python
print(2 ** 4)
```

#### Example 4

```python
budget = 1500
spent = 450
print(budget - spent)
```

#### Practice exercises

1. Find the total cost of 3 notebooks if one costs 120 rupees.
2. Divide 17 mangoes equally among 4 friends. Find equal share and leftover.
3. Calculate `5 + 2 * 3`.

#### Solutions

```python
print(3 * 120)
```

```python
print(17 // 4)
print(17 % 4)
```

```python
print(5 + 2 * 3)
```

### Major Topic: Loops

#### Example 1

```python
for number in range(1, 6):
    print(number)
```

#### Example 2

```python
for city in ["Lahore", "Karachi", "Quetta"]:
    print(city)
```

#### Example 3

```python
count = 1
while count <= 3:
    print("Study time")
    count += 1
```

#### Practice exercises

1. Print numbers from 1 to 10.
2. Print three favorite foods from a list.
3. Use a `while` loop to print `Bismillah` 5 times.

#### Solutions

```python
for i in range(1, 11):
    print(i)
```

```python
foods = ["Biryani", "Samosa", "Mango"]
for food in foods:
    print(food)
```

```python
count = 1
while count <= 5:
    print("Bismillah")
    count += 1
```

### Major Topic: Lists and Dictionaries

#### Example 1

```python
fruits = ["mango", "banana", "orange"]
print(fruits[0])
```

#### Example 2

```python
students = ["Ali", "Ayesha"]
students.append("Hamza")
print(students)
```

#### Example 3

```python
prayer_times = {"Fajr": "5:00", "Maghrib": "6:45"}
print(prayer_times["Fajr"])
```

#### Example 4

```python
marks = {"Math": 78, "Science": 81}
marks["English"] = 74
print(marks)
```

#### Practice exercises

1. Make a list of three cities.
2. Add one new fruit to a fruit list.
3. Make a dictionary with two subjects and their marks.

#### Solutions

```python
cities = ["Lahore", "Multan", "Peshawar"]
print(cities)
```

```python
fruits = ["mango", "banana"]
fruits.append("apple")
print(fruits)
```

```python
marks = {"Math": 90, "Urdu": 85}
print(marks)
```

---

## 9. Assessment Strategy

### Module-by-module assessment model

Each module should include:

- 5-question oral review
- 5 to 10 short quiz items
- 1 coding checkpoint
- 1 mini application task

### Sample quiz questions by module

#### Module 1: Strings

Multiple choice:

1. Which of the following is a string?
   - A. `25`
   - B. `"25"`
   - C. `True`
   - Answer: B

2. What does `len("Lahore")` return?
   - A. 5
   - B. 6
   - C. 7
   - Answer: B

Short answer:

1. What is a string?
2. Write one line of code to print `Pakistan`.

#### Module 2: Variables and Input

Multiple choice:

1. Which line stores a name in a variable?
   - A. `print = "Ali"`
   - B. `name = "Ali"`
   - C. `"Ali" = name`
   - Answer: B

2. What does `input()` do?
   - A. prints output
   - B. removes spaces
   - C. takes data from the user
   - Answer: C

Short answer:

1. What is a variable?
2. Why do we use meaningful variable names?

#### Module 3: Data Types

Multiple choice:

1. What type is `14`?
   - A. `str`
   - B. `int`
   - C. `float`
   - Answer: B

2. What type does `input()` return?
   - A. `str`
   - B. `int`
   - C. `bool`
   - Answer: A

Short answer:

1. What is the difference between `int` and `float`?
2. Why do we convert input before calculation?

#### Module 4: Operators

Multiple choice:

1. Which operator gives a remainder?
   - A. `//`
   - B. `%`
   - C. `**`
   - Answer: B

2. What is the result of `2 + 3 * 4`?
   - A. 20
   - B. 14
   - C. 24
   - Answer: B

Short answer:

1. Explain the difference between `/` and `//`.
2. Write an example using `%`.

#### Module 5: If Statements

Multiple choice:

1. Which symbol checks equality?
   - A. `=`
   - B. `==`
   - C. `!=`
   - Answer: B

2. What happens if an `if` condition is false and there is no `else`?
   - A. Python crashes
   - B. The block is skipped
   - C. It becomes true
   - Answer: B

Short answer:

1. What is a condition?
2. Why is indentation important?

### Capstone projects

#### Project 1: School Canteen Bill Calculator

Concepts:

- variables
- input
- numbers
- operators
- formatted output

#### Project 2: Student Report Card

Concepts:

- input
- conversion
- `if` statements
- lists
- functions

#### Project 3: Rainfall and Crop Helper

Concepts:

- input
- conditions
- loops
- functions
- dictionaries

#### Project 4: Prayer Routine Tracker Using Sample Data

Concepts:

- lists
- dictionaries
- loops
- conditions

Note:

This should be framed as a sample learning project, not as a source of real religious timing decisions.

### Self-assessment rubric for students

Students rate themselves from 1 to 4:

- 1: I need a lot of help
- 2: I can do some parts
- 3: I can do it by myself
- 4: I can teach another student

Rubric areas:

- I can read code
- I can predict output
- I can fix small mistakes
- I can write my own short program
- I can explain what my program does

---

## 10. Resource Recommendations

### Best tools for limited-resource Pakistani classrooms

- Python IDLE
  - already simple
  - lightweight
  - works offline

- Thonny
  - beginner friendly
  - good variable view
  - useful for teachers

- VS Code
  - only for labs with stronger computers and teacher support

### Browser-based tools when internet is available

- Replit
- Trinket
- PythonTutor for visualization

### Offline alternatives

- Python installed with IDLE
- Thonny portable setup on lab machines
- printed worksheets
- projector-based live coding when devices are limited
- paired programming if student-to-computer ratio is low

### Practical recommendation

For most Pakistani school and Madrasa environments:

1. Use Thonny where possible.
2. Keep IDLE as backup.
3. Avoid dependence on constant internet access.

---

## 11. Teacher Guidance Notes

### General teaching tips

- Start every lesson with a 2-minute recap.
- Ask students to predict output before running code.
- Use pair discussion for debugging questions.
- Keep typing load low for weak typists.
- Repeat key ideas using both code and real-life examples.

### Common misconceptions and responses

- Misconception: quotes are optional for text
  - Response: show Python error and compare text vs numbers

- Misconception: `=` means compare
  - Response: teach `=` as store, `==` as compare

- Misconception: `input()` gives numbers automatically
  - Response: demonstrate with `type()`

- Misconception: indentation is decoration
  - Response: show how changing indentation changes meaning

- Misconception: loops stop on their own
  - Response: trace counter values on the board

### Extension activities for advanced students

- Convert a simple print-based program into a function-based program
- Add input validation using `while`
- Create a mini quiz with score counting
- Expand a dictionary-based student record

### Time estimates by module

- Module 0: 1 to 2 weeks
- Module 1: 2 weeks
- Module 2: 2 weeks
- Module 3: 2 weeks
- Module 4: 2 weeks
- Module 5: 2 to 3 weeks
- Module 6: 2 to 3 weeks
- Module 7: 2 weeks
- Module 8: 3 weeks
- Module 9: 2 to 3 weeks

Total recommended course length:

- 19 to 23 teaching weeks for a steady school schedule

---

## 12. Action Items for Course Implementation

### High-priority actions

1. Reorganize the current material into the redesigned module order.
2. Remove duplicated concepts from `Variables`, `Data Types`, and `Operators`.
3. Standardize all files to UTF-8 encoding.
4. Replace dense script-style lessons with concise teacher-ready lesson notes.
5. Add measurable learning objectives and checkpoints to every lesson.

### Medium-priority actions

1. Build one worksheet and one quiz for each module.
2. Create one offline-friendly code pack per module.
3. Add more Pakistani school-life examples alongside Madrasa examples.
4. Delay advanced collection topics until students master lists.

### Pilot plan

1. Pilot Modules 1 to 3 with a small mixed group.
2. Observe pacing around variables, input, and type conversion.
3. Record the most common student errors.
4. Refine lesson timing before converting the full course.

### Final recommendation

Do not patch the current course lightly. The better path is to treat the existing material as source content, preserve the best local examples, and rebuild the learner experience around a cleaner, scaffolded progression.
