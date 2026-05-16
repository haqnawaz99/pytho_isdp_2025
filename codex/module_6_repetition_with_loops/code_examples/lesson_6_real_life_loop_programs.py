pages_per_day = 2

for day in range(1, 6):
    print(f"Day {day}: read {pages_per_day} pages")

expense = 100
total = 0

for day in range(1, 6):
    total = total + expense

print(f"Total weekly expense: {total}")

over = 1

while over <= 3:
    print(f"Over {over}: keep batting carefully")
    over += 1
