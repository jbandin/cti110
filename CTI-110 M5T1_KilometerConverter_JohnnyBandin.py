# This program converts kilometers to miles
# 2 July 2017
# CTI-110 M5T1_KilometerConverter
# Johnny Bandin

# Make the variable for the conversion factor
conversion_factor = 0.6214

def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)

def show_miles(km):
    # Calculate miles.
    miles = km * conversion_factor

    # Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

main() 
