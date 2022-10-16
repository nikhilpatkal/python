import random
no=int(input("how many number of OTP you want "))
l=[0,1,2,3,4,5,6,7,8,9]
p=[]
a=""
for i in range(no):
    value=random.choice(l)
    p.append(value)

for i in p:
    a=a+str(i)
print(f"your password is {a}")
    
