def show_welcome(name):
    print(f"Welcome {name}")

def calculate_total(price, quantity):
    return price * quantity

def grade_message(marks):
    if marks >= 80:
        return "Excellent"
    elif marks >= 50:
        return "Pass"
    else:
        return "Fail"

show_welcome("Ayesha")
print(calculate_total(120, 4))
print(grade_message(72))
