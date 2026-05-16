# Project 3 - School Fee Calculator (SOLUTION)

print("=== School Fee Calculator ===")


def calculate_fee(monthly_fee, months):
    return monthly_fee * months


student_name = input("Student name: ")
monthly_fee = float(input("Monthly fee (rupees): "))
months = int(input("Number of months: "))

total = calculate_fee(monthly_fee, months)
print(f"Student: {student_name}")
print(f"Monthly fee: {monthly_fee} rupees")
print(f"Months: {months}")
print(f"Total fee: {total} rupees")

if total > 10000:
    discount = total * 0.05
    final_amount = total - discount
    print(f"Discount 5%: -{discount} rupees")
    print(f"Amount to pay: {final_amount} rupees")
else:
    print("No discount applied.")
