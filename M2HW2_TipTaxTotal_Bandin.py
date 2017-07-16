# Tip Tax and Total Project
# 11 JUN 2017
# CTI-110 M2HW2 - Tip Tax Total
# Johnny Bandin
# Calculate the charge for food
total = float(input('Enter the total amount of meal purchased:'))

#Calculate the 18 percent tip 
tip = 0.18*total

#Calculate the 7 percent sales tax
sales_tax = 0.07*total

#Calculate the total amount
total_amount = total + tip + sales_tax


#Display each amounts and total
print (' 18 percent tip $%s' % format(tip,'.2f'))

print ('7 percent sales tax $%s' % format (sales_tax, '.2f'))

print ('total amount = $%s' % format (total_amount, '.2f'))

              
