# A program to accept percentage of a student and display grade
perc=float(input("enter percentage of a student : ")) # statement1
if perc > 85:                                   #condition1
    print ('A')
elif perc > 70 and perc <=85:                   #condition2
    print ('B')
elif perc > 60 and perc<=70:                    #condition3
    print ('C')
elif perc > 45 and perc<=60:                    #condition4
    print ('D')
else:
    print ('E')
    
