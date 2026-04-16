"""
Pizza Pay Calculator
Calculates total earnings based on trips and minutes
"""

# PSEUDOCODE:
# START
# INPUT number of trips
# INPUT number of minutes
# CALCULATE trip_pay = trips * 1.45
# CALCULATE minute_pay = minutes * 0.95
# CALCULATE total_pay = trip_pay + minute_pay
# DISPLAY total_pay
# END

# Constants
PAY_PER_TRIP = 1.45
PAY_PER_MINUTE = 0.95

# Input
number_of_trips = int(input("Enter number of trips: "))
number_of_minutes = int(input("Enter number of minutes driven: "))

# Processing
trip_pay = number_of_trips * PAY_PER_TRIP
minute_pay = number_of_minutes * PAY_PER_MINUTE
total_pay = trip_pay + minute_pay

# Output
print(f"Total pay: ${total_pay:.2f}")