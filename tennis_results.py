"""
Tennis Results Program
Determines match result based on scores
"""

# PSEUDOCODE:
# START
# INPUT player_score
# INPUT opponent_score
# IF player_score > opponent_score
#     DISPLAY "You win"
# ELSE IF player_score < opponent_score
#     DISPLAY "You lose"
# ELSE
#     DISPLAY "Draw"
# IF total games >= 8
#     DISPLAY "Fast match"
# END

# Input
player_score = int(input("Enter your score: "))
opponent_score = int(input("Enter opponent score: "))

# Decision structure
if player_score > opponent_score:
    print("You win!")
elif player_score < opponent_score:
    print("You lose!")
else:
    print("It's a draw!")

# Extra condition
total_games = player_score + opponent_score

if total_games >= 8:
    print("Fast match!")

# Explanation:
# I used an if-elif-else structure because there are three outcomes:
# win, lose, or draw.