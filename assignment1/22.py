st=input("enter the string")
count=0
count1=0
for i in st:
    if i.isalpha():
        count=count+1
    else:
        count1=count1+1
print("alpha count");print(count)
print("number count");print(count1)
