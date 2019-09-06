num1=int(input("enter the number1"))
temp=num1
x=0
while(num1):
    i=num1%10
    x=x*10+i
    num1=int(num1/10)
print(x)
if x==temp:
    print("palindrome")
else:
    print("not a palindrome")