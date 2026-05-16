def weather_advice(temperature, rainfall):
    if temperature >= 40:
        return "Stay hydrated"
    elif rainfall > 0:
        return "Carry an umbrella"
    else:
        return "Weather looks fine"

temperature = float(input("Enter temperature: "))
rainfall = float(input("Enter rainfall: "))

print(weather_advice(temperature, rainfall))
