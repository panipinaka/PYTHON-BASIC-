num=int(input("enter the number"))
tot=0
while(num):
    i=num%10
    tot=tot+i
    num=int(num/10)  
print(tot)
        
