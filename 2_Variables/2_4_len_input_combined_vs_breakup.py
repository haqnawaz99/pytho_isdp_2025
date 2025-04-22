# len_input_examples.py

# 🔹 Example 1: Count letters in student's name (One-line)
print("Number of letters in your name is:", len(input("Enter your name: ")))

# 🔸 Example 1 (Break-up version)
name = input("Enter your name again: ")
name_length = len(name)
print("Number of letters in your name is:", name_length)

# --------------------------------------------

# 🔹 Example 2: Count characters in favorite Surah (One-line)
print("Characters in your favorite Surah:", len(input("Enter your favorite Surah name: ")))

# 🔸 Example 2 (Break-up version)
surah = input("Enter the Surah name again: ")
surah_length = len(surah)
print("Characters in your favorite Surah:", surah_length)

# --------------------------------------------

# 🔹 Example 3: Count characters in a short sentence (One-line)
print("Characters in your sentence:", len(input("Write a short sentence: ")))

# 🔸 Example 3 (Break-up version)
sentence = input("Write the sentence again: ")
sentence_length = len(sentence)
print("Characters in your sentence:", sentence_length)
