lis=[1,2,3,4,5,6]
lis2=[2,3,5,4,1,6]
flag=1
for i in lis:
    if i in lis2:
        continue
    else:
        flag=0
        break
if flag==1:
    print("same list")
else:
    print("not a same list")
    
