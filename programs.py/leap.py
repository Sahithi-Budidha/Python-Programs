year=int(input("enter year:"))

if (year%100==0):
    if(year%400==0):
        print("it is a leap year.")
    else:
        print("not a leap year.")
if(year%100 != 0):
    if(year%4==0):
        print("it is a leap year.")
    else:
        print("not a leap year.")
