# Project 2 - Maktaba Book List (SOLUTION)

print("=== Maktaba Book List ===")

books = ["Tafsir Ibn Kathir", "Sahih Bukhari", "Riyadus Saliheen"]

print("Books in Maktaba:")
for i in range(len(books)):
    print(f"{i + 1}. {books[i]}")

new_book = input("Enter a book to add: ")
books.append(new_book)

print("--- Updated list ---")
for i in range(len(books)):
    print(f"{i + 1}. {books[i]}")

print(f"Total books: {len(books)}")
