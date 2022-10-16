l_number=[12,23,24,25,345,57,23]
l_prime=[]
l_not_prime=[]
for j in l_number:
    flag= False
    for i in range(2,j):
        if j% i==0:
            flag=True
            break
    if flag==True:
        l_not_prime.append(j)
    else:
        l_prime.append(j)
print("prime number")
print(l_prime)
print("non prime number")
print(l_not_prime)
