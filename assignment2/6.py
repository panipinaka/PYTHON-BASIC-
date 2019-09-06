lis=[]
val=1
while val==1:
    val=int(input("if u want to add tuple to the list press 1 else press 0"))
    if val==1:
        n=int(input("enter the integer value"))
        m=n*n
        lis.append(tuple((n,m)))
        print(lis)
    else:
        print(lis)
