weight = float(input('Enter weight in pounds: '))
height = float(input('Enter height in inches: '))
bmi = (weight / (height * height)) * 703.0
print(' Your BMI is', (bmi)) 

if bmi >= 0:
    print ('Your weight status is under weight')
else:
    if bmi >= 18.5: 
        print ('Your weight status is optimal weight')
    else:
        if bmi >= 25:
            print (' Your weight status is over wieght')
