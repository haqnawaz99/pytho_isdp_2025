item_price = 250
quantity = 4
total_cost = item_price * quantity

budget = 5000
book_price = 850
books = 2
stationery = 600

spent = (book_price * books) + stationery
left = budget - spent

print(f"Total cost: {total_cost}")
print(f"Money left: {left}")
