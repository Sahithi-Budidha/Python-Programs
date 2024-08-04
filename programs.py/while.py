#defining the variables
day=0
squats=0
total=0
print("enter no of suqats u did for the each day specified below:");

#loop
while day<=6:
    day=day+1
    squats=int(input("enter the no of squats on day {}:".format(day)))
    total=total+squats

#outside the while looop
avg= total/day
print("in the last {} days, you did an avg of {} squats".format(day,avg))
    
