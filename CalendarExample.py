import calendar
if(calendar.isleap(int(input("Enter year")))):
   print("It is leap year")
else:
   print("It is not a leap year")
print(calendar.month(2022,2))
print(calendar.month(2022,4))
print(calendar.leapdays(2000,2010))

