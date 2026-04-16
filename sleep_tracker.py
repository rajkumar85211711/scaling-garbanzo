"""
Sleep Tracker Program
Tracks sleep for 5 days and calculates sleep debt
"""

# PSEUDOCODE:
# START
# SET total_sleep = 0
# FOR each day from 1 to 5
#     REPEAT until valid input (0–24)
#         INPUT sleep_hours
#     ADD sleep_hours to total_sleep
# CALCULATE sleep_debt = (5 * 8) - total_sleep
# DISPLAY results
# END

# Constants
DAYS = 5
DESIRED_SLEEP = 8

total_sleep = 0

# Loop for 5 days
for day in range(1, DAYS + 1):
    while True:
        sleep_hours = float(input(f"Enter sleep hours for day {day}: "))
        
        if 0 <= sleep_hours <= 24:
            break
        else:
            print("Invalid input. Enter between 0 and 24.")

    total_sleep += sleep_hours

# Calculate sleep debt
desired_total = DAYS * DESIRED_SLEEP
sleep_debt = desired_total - total_sleep

# Output
print(f"Total sleep: {total_sleep}")
print(f"Sleep debt: {sleep_debt}")

# Explanation:
# A for loop is used to repeat input for 5 days.
# A while loop is used for validation to ensure input is between 0 and 24.