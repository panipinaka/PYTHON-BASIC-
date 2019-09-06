st1=input("enter the string1")
st2=input("enter the string2")
count1=0
count2=0
for i in st1:
    count1=count1+1

for i in st2:
    count2=count2+1
if count1>count2:
    print(st1)
else:
    print(st2)
