# Average test grades.
# 9 July 17
# CTI-110 M5HW1-Test Average and Grade
# Johnny Bandin

#Define the main function
def main():
    average=calc_average()
    determine_grade(average)
#Function that calculates the user's average input.
def calc_average():
    List=[]
    print('''This Program will ask for 5 test scores in a row.''')
    print('''Enter "-1" at any time to quit.''')
    for x in range(5):
        test=float(input('Enter test score:  '))
        if test == -1:
            break
        List.append(test)
        print(List)
    if x == 4:
        average=(sum(List)/5)
        return average
        print(average)
    else:
        return -1
#Function that finds the user's average grade.
def determine_grade(x):
    if x >=90:
        print("Congrats.  You got an A with an average of %s."% x)
    elif x >= 80 and x < 90:
        print("nice job.  You recieved a B with an average of %s." %x)
    elif x >= 70 and x < 80:
        print("You achieved a C with an average of %s, still better than most." % x)
    elif x >= 60 and x < 70:
        print("You were given a D with an average of %s, keep trying and dont give up." % x)
    elif x >= 0 and x < 60:
        print('You straight got a F with an average of %s, you should quit school kiddo' % x)
    else:
        print('stopping Program')
main()
    
