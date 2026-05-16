# Module 5 - Extension (OPTIONAL)
# Learning objective: break stops a loop early

# break in while
n = 1
while n <= 10:
    if n == 6:
        break
    print(n)
    n += 1
print("Loop stopped at 6")

# break in for
for i in range(1, 8):
    if i == 5:
        break
    print(i)

# Simple menu (type quit to stop)
# Uncomment to run interactively:
# while True:
#     cmd = input("Enter command (quit to exit): ")
#     if cmd == "quit":
#         break
#     print("You typed:", cmd)
