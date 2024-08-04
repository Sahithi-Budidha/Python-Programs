num=int(input("Enter the num:"))
fact = 1

for x in range(1,num+1):
    fact=fact*x
print("the factorial of {} is : {}".format(num,fact))
