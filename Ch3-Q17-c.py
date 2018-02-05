user_year=int(input("Enter the year in YYYY format: "))
if ((user_year%400!=0) and (user_year%100==0)) or (user_year%4!=0) :
   print (str(user_year)+" is not a leap year")
else:
   print (str(user_year)+" is a leap year")