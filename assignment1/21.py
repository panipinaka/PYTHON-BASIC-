st=input("enter the string")
count1=0
count2=0
for i in st:
    if i.isupper():
        count1=count1+1
    else:
        count2=count2+1
print("uppercount=");print(count1)
print("lowercount=");print(count2)