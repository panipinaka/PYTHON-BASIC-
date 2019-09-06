#num1=str(input("enter the number1"))
num2=int(input("enter the number2"))
#abc=num.reverse
x=0
while(num2):
    i=num2%10
    x=x*10+i
    num2=int(num2/10)
print(x)