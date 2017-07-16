# This program converts feet to inches
# 2 July 2017
# CTI-110 M5T2_FeetToInches
# Johnny Bandin

# Constant for the number of inches per foot.
inches_per_foot = 12

# Main function
def main():
    # Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # Convert that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# the feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * inches_per_foot

# Call the main function.
main()
