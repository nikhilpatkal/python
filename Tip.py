
amount=int(input("enter Bill amount"))
Tip=int(input("how many tip you want"))
person=int(input("how many person in group:"))
Tip=(amount*Tip)/100
Tip=amount+Tip
Tip=Tip/person
print("amount for each person: ",round(Tip,2))
