# Project 7 (OPTIONAL) - Rainfall Helper (SOLUTION)

print("=== Rainfall Helper (mm) ===")

city = input("City name: ")
rainfall = float(input("Rainfall today (mm): "))

if rainfall > 50:
    advice = "Heavy rain - stay indoors if possible"
elif rainfall > 10:
    advice = "Carry an umbrella"
else:
    advice = "Light or no rain - normal day"

print(f"{city}: {rainfall} mm rainfall.")
print(f"Advice: {advice}")

if rainfall > 30:
    print("Farmers: check drainage in fields.")
