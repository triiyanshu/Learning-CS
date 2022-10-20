"""
Write a program ot promt the user for hours and rate per hour,
using input to compute gross pay.
Use 35 hours and a rate of 2.75 per hour to,
test the porgram (the pay should be 96.25). 
You should use input to read a string and float() to,
convert the string to a nubmer. 
Do not worry about the error checking or bad user.
Also Add 1.5 times the hourly rate for hours worked above 40 hours.

"""
# StringHours = sh
# StringRate = sr
# FloatRate = fr
# FloatHours = fh
# Payment = py
# Payment with overtimebonus = pyb
# OverTime = ovtm
# OverTime Bonus = ovtmb

sh = input('Number of Hours you worked for? \n Enter Hours: \n')
try:
     fh = float(sh)
except:
    print('Error, Please enter numeric input.\n')
    quit()
    
sr = input('What is the rate of payment? \n Enter Rate: \n')
try:
    fr = float(sr)
except:
    print('Error, Please enter numeric input.\n')
    quit()
    
py = fr * fh
if fh <= 0 :
    print ('INVALID INPUT.\n')
    
elif fh >= 40 :
    ovtm = fh - 40
    ovtmb = ovtm * 0.5
    pyb = py + ovtmb
    print('You have worked overtime for', ovtm, 'hours.\n')
    print('Your overtime bonus is ', ovtmb, 'rupees.\n')
    print('Your total payment is ', pyb, 'rupees.\n')
    
else :
    print('You worked for ', fh, 'hours.\n')
    print ('Your total payment is ', py, 'rupees.\n')
    
exit()
