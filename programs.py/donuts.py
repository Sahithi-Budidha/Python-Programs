'''price=int(input("Enter the price of a donut: RS."))
quantity= int(input("Enter the no. of donuts: "))
amount= price*quantity

if amount>1000:
    print("yayy disininfiw")
    discount= amount*10/100
    amount=amount-discount
else:
    print("5%")
    discount=amount*5/100
    amount= amount-discount
print("total amount is: RS.",amount)'''

price=105.50
qty=7000
amount=price*qty
if amount>10000:
   print ("10% discount applicable")
   discount=amount*10/100
   amount=amount-discount
elif amount>5000:
    print ("5% discount applicable")
    discount=amount*5/100
    amount=amount-discount
elif amount>2000:
    print ("2% discount applicable")
    discount=amount*2/100
    amount=amount-discount
elif amount>1000:
     print ("1% discount applicable")
     discount=amount/100
     amount=amount-discount
else:
    print ("no discount applicable")
print ("amount payable:",amount)
