import random as r
ab=[]
j=10
i=1
while len(ab)<10:
    if j<101:
        a=r.randint(i,j)
        i=j+1
        j=j+10
        ab.append(a)
print(ab)
    