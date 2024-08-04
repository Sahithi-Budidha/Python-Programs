#to check whether i have money to splurge on the new smartphone

def verdict(m1,m2,m3):
    total=m1+m2+m3
    if total>=15000:
        print("Congratulations! you have enough money to get a new smartphone.")
    else:
        print("oops...You--unfortunately--don't have enough money.")
    return

gift=int(input("Gift Money from Fam:"))
savings=int(input("enter ur savings:"))
internship=int(input("Enter the amount earned:"))
verdict(gift,savings,internship)
