# This script calculates the win percentage of a sports team.
# The user is prompted to enter the team's name, the number of games won, and the number of games lost.
# The script calculates the win percentage as (won / (won + lost)) * 100, rounds it to one decimal place, and prints the result.

name = input("Enter the name of team: ")
won = int(input("Enter the number of games won: "))
lost = int(input("Enter the number of games lost: "))

penc = won / (won + lost) * 100

print(name, "won", str(round(penc, 1)) + "% of their games.")
