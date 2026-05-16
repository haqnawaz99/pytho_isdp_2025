temperature = float(input("Enter temperature: "))

if temperature >= 40:
    print("Stay hydrated and avoid too much sun.")
elif temperature >= 30:
    print("It is a hot day.")
else:
    print("Weather is moderate.")

runs = int(input("Enter cricket runs: "))

if runs >= 100:
    print("Century")
elif runs >= 50:
    print("Half century")
else:
    print("Keep batting")
