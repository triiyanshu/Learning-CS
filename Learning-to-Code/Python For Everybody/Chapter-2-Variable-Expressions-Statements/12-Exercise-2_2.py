# Write a program ot promt the user for hours and rate per hour using input to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the porgram (the pay should be 96.25). 
# You should use input to read a string and float() to convert the string to a nubmer. 
# Do not worry about the error checking or bad user

Hours = input("Enter Hours: ") #Promts the user to enter the number of hours.
# RatePerHour = float(2.75) #Rate per hour is pre-defined.
RatePerHour = input("Enter Rate per Hours: ")
RatePerHour = float(RatePerHour)
Hours = int(Hours)
# print("Entered Hour is ",Hours) #Prints the user input to confirm.
print("Gross Pay is ", Hours*RatePerHour)