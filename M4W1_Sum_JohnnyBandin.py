# Sum of Numbers Chapter 4 Exercise 8
# 26 JUN 17
# CTI-110 M4HW1 - Sum of Numbers
# Johnny Bandin

# Assign a value to the variables
A = 0
B = 0

# If input is positive the loop will continue to run
while A >= 0:
    A = float(input('A positive number to add to each other put a negative number to stop the loop and display the total: '))
    if A > 0:
        B = A + B
    if A < 0:
        print(' The sum of all positive values is',B)
    
