# Project 6 (OPTIONAL) - Cricket Score Helper (SOLUTION)

print("=== Cricket Score Helper ===")


def milestone_message(runs):
    if runs >= 100:
        return "Century! Shahbash!"
    if runs >= 50:
        return "Half century! Great batting!"
    return "Keep practicing - every run counts!"


runs = int(input("Enter runs scored: "))
print(f"Runs: {runs}")
print(milestone_message(runs))

# Bonus: team total
team_mate = int(input("Team mate runs: "))
total = runs + team_mate
print(f"Partnership total: {total}")
