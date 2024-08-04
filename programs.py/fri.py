def food(f,num):
    tip=0.1*f
    f=tip+f
    avg=f/num
    print("Each has to pay:{}".format(avg))
friend=int(input("Enter num of friends:"))
total=int(input("Enter total bill:"))
food(total,friend)
