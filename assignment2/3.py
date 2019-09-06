lis=[1,2,34,4,3,6,7,8,9,78,21,43]
even=[]
odd=[]
for i in lis:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)