def cumulative_sum(lis):
    abc=[]
    tot=0
    for i in lis:
        tot=tot+i
        abc.append(tot)
    print(abc)
lis=[1,2,4]
cumulative_sum(lis)
        
