import random as r
ab=[]
while len(ab)<5:
    a=r.randint(1,20)
    if a in ab:
        continue
    else:
        ab.append(a)
print(ab)

