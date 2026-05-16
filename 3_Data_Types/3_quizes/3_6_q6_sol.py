# 3_1_q6_sol.py

# =======================================================
# ✅ Task 6: Book Price Calculator (Solution)
# =======================================================

price = int(input("Enter price of one book: "))
quantity = int(input("Enter number of books: "))
total_price = price * quantity

# Using +
print("Total price is " + str(total_price) + " rupees.")

# Using f-string
print(f"Total price is {total_price} rupees.")