"""
Rewrite your pay computation ot give the employee 1.5 times the hourly rate for hours worked
above 40 hours.
Enter Hours : 45
Enter Rate : 10
Pay : 475.0
"""
#PREVIOUS PROGRAM LINK
#https://github.com/triiyanshu/Learning-CS/blob/1a6fbb70194b70d118f533b5cb62dc141137e671/Intro%20CS/Python%20For%20Everybody/Chapter-2-Variable-Expressions-Statements/12-Exercise-2_2.py

Hours = int(input("Enter Hours: ")) #Prompts the user to enter the number of hours they worked.
RatePerHour = float(2.75)
RatePerHourifgreaterthan40hours = float(1.5)
Hours = int(Hours)
if Hours <= 0:
    print("Please Provide Valid Input for Hours")
elif Hours > 40:
    print("Gross Pay is", Hours*RatePerHourifgreaterthan40hours)
else:
    print("Gross Pay is", Hours*RatePerHour)
