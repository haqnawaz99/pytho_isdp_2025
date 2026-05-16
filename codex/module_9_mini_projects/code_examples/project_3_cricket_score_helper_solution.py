def score_message(runs):
    if runs >= 100:
        return "Century"
    elif runs >= 50:
        return "Half century"
    else:
        return "Below fifty"

player = input("Enter player name: ")
runs = int(input("Enter runs: "))

print(f"{player}: {score_message(runs)}")
