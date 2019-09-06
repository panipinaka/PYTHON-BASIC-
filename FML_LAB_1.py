#!/usr/bin/env python
# coding: utf-8

# # FML LAB PYTHON BASIC

# In[40]:




num=int(input("enter the number"))
if num==5:
    print(num," is equal to 5")
if num<6:
    print(num," is less then 6")
if num>4:
    print(num," is grater then 4")
if num<=5:
    print(num," is less then or equal to 5")
if num>=5:
    print(num," is grater then or equalto 5")
if num!=4:
    print(num," is not equal to 5")


# In[9]:


num=int(input("enter the num"))
if num<2:
    print("below 2")
elif num>=2:
    print("2 or more")
else:
    print("sumthing else")


# In[23]:


astr="hello bob"
try:
    istr=int(astr)
except:
    istr=-1    
print('frist',istr)
astr='123'
try:
    istr=int(astr)
except:
    istr=-1
print('second',istr)


# In[24]:


astr='bob'
try:
    print('hello')
    istr=int(astr)
    print('there')
except:
    istr=-1
print('done',istr)


# In[38]:


astr=input("enter the number")
try:
    istr=int(astr)
except:
    istr=-1
if istr>0:
    print("good job")
else:
    print("kindly enter the number")


# In[33]:


hour=float(input("enter the hours"))
rate=float(input("enter the rate"))
if hour>40:
    extime=hour-40
    pay=40*rate+extime*(rate*1.5)
else:
    pay=hour*rate
print("pay is",pay)


# In[41]:


while True:
    line=input('<')
    if line=='done':
        break
    print(line)
print('done!')


# In[47]:


while True:
    line=input('<')
    if line[0]=='#':
        continue
    if line=='done':
        break
    else:
        break
    print(line)
print('done!')


# # LISTS

# In[48]:


friends=['ajith','chandan','shaheel']
for i in friends:
    print(i)


# In[50]:


friends=['ajith','chandan','shaheel']
print('before')
for i in friends:
    print(i)
print('after')


# In[51]:


large=0;
lis=[10,20,49,29,102,2839,13913193]
for i in lis:
    if i>large:
        large=i
print(large)


# In[54]:


large=0
num=29
lis=[10,20,49,29,102,2839,13913193]
if num in lis:
    print("true")
else:
    print("false")


# In[105]:


num=int(input("enter the number"))
if num is 5:
    print(num," is equal to 5")
if num is not 5:
    print(num," is not equal to 5")


# # DICTIONARY 

# In[95]:


sales={
    'price':3.14,
    'no_items':10,
    'person':"abc"
}
sales_statement='{} brought {} items at price {} total {} '
print(sales_statement.format(sales['person'],
                            sales['no_items'],
                            sales['price'],
                            int(sales['price']*sales['no_items'])))


# In[85]:


import time as t
import datetime as d
t.time()
ac=d.timedelta(days=100)
print(d.date.today()-ac)


# In[104]:


class Person:
    inst="manipal school of info science"
    def set_name(self,new_name):
        self.name=new_name
    #def set_loc(self,new_loc):
     #   self.loc=new_loc
person=Person()
person.set_name("abc")
#person.set_loc("shimoga")
person.loc='shimoga'
print('{} lives in {} and studies in {}'.format(person.name,person.loc,person.inst))


# In[129]:


abc=[21,32,43,65,63,87698,52,67]
cdf=[12,34,13,43,35,42,242,23433]
low=map(min,abc,cdf)
abc=list(low)
abc.sort()
for i in abc:
    print(i)


# # LAMBDA

# In[118]:


my_fun=lambda a,b,c: a+b+c
print(my_fun(5,3,5))


# In[116]:


def split_title_and_name(person):
     print(person.split()[0]+ ' '+person.split()[-1])
people=['Dr abc','dr new','dr eqe']
for abc in people:
    split_title_and_name(abc)


# In[31]:


my_fun=lambda abc:abc.split()[0]+ ' '+abc.split()[-1]
people=['Dr abc','dr new','dr eqe']
for abc in people:
    print(my_fun(abc))


# # NUMPY ARRAY,MAP

# In[69]:


import numpy as np
a = np.arange(6).reshape(2,3)
print(a)
for i in np.nditer(a):
    print(i)
    


# In[10]:


def calsquare(n):
    return n*n
lis=1,2,3
res=map(calsquare,lis)
for i in res:
    print(i)


# In[23]:


num1=[1,2,3]
num2=[1,2,3]
my_fun=map(lambda a,b: a+b,num1,num2)
print(list(my_fun))


# In[28]:


person=['Dr abc','dr new','dr eqe']
def split_title_and_name(person):
    title=person.split()[0]
    lastname=person.split()[-1]
    return '{} {}'.format(title,lastname)
list(map(split_title_and_name,person))


# In[33]:


lis=[num for num in range(0,20) if num%2==0]
lis


# In[40]:


dic=[num*num2 for num in range(1,11) for num2 in range(1,11) ]
print(dic)


# In[41]:


import numpy as np
arr=np.arange(10)
print(arr)
b=arr.reshape(2,5)
print(b)


# In[44]:


import numpy as np
lis=[1,2,3,4,5,6]
arr=np.array(lis)
arr


# In[55]:


arr=np.linspace(1,7,4)
print(arr.reshape(2,2))


# In[62]:


np.eye(3)


# In[76]:


np.zeros((3,3),int)


# In[80]:


arr=np.arange(16)
b=arr.reshape(4,4)
print(b)
print()
print(np.diag(b))


# In[131]:


np.ones((3,3),int)


# In[86]:


p=np.ones((3,3),int)
np.vstack((p,p*5))


# In[130]:


np.hstack((p,p*4))


# In[132]:


r=np.arange(100)
r.resize((10,10))
print(r)
print()
print(np.diag(r),'\n')
print(np.diag(r,1),'\n')
print(np.diag(r,-1),'\n')
print(r[:3,:3])


# In[2]:


import numpy as np
old=np.array([[1,1,1],[1,1,1]])

new=old
new[0:2, :1]=0
print(new)


# In[22]:


old=np.array([[1,1,1],[1,1,1],[1,1,1]])
new=old
new[1:2,1:2]=0
print(new)


# In[25]:


old=np.arange(100)
old.resize((10,10))
new=old
for i in range(10):
    if i%2!=0:
        print(i)
        new[i]=0
print(new)


# # PANDAS

# In[28]:


import pandas as pd
from pandas import Series
animals=['Tiger','bear',None]        
pd.Series(animals)



# In[29]:


num=[1,2,None]
pd.Series(num)


# In[35]:


sports={'archery':'bhuthan',
       'golf':'Scotland',
       'sumo':'japan',
       'taekwondo':'south Korea',
       'boxing':'India'}
s=pd.Series(sports)
s


# In[36]:


s.iloc[4]


# In[39]:


s.loc['golf']


# In[42]:


s['boxing']


# In[46]:


sports={90:'bhuthan',
       99:'Scotland',
       98:'japan',
       102:'south Korea',
       104:'India'}
s=pd.Series(sports)
s


# In[47]:


s[99]


# In[51]:


s=pd.Series([100.00,102.00,103.00,104.00])
s


# In[52]:


total=np.sum(s)
total


# In[63]:


import random
s=pd.Series(np.random.randint(100,10000,10))
s


# In[65]:


len(s)


# In[78]:


get_ipython().run_cell_magic('timeit', '-n 100', 'summary=0\nfor item in s:\n    summary+=item')


# In[79]:


get_ipython().run_cell_magic('timeit', '-n 100', 'summary=np.sum(s)')


# In[83]:


s=pd.Series([1,2,3,4,5])
s.loc['name']='Pinaka'
s


# In[110]:


olympics=pd.Series({'bhuthan':'archery',
       'Scotland':'golf',
       'japan':'sumo',
       'south Korea':'taekwondo',
        'Brazil':'football'})
cricket=pd.Series({'India':'Cricket',
                  'Australia':'Cricket'})
Cricket_in_olympics=olympics.append(cricket)
Cricket_in_olympics.sort_index()


# # DATAFRAME AND DATA STRUCTURE

# In[6]:


import pandas as pd
purchase_1=pd.Series({'Name':'Chris',
                     'Item Purchased':'Dog Food',
                     'Cost':34})
purchase_2=pd.Series({'Name':'Ajith',
                     'Item Purchased':'food',
                     'Cost':342})
purchase_3=pd.Series({'Name':'shaheel',
                     'Item Purchased':'drinks',
                     'Cost':400})
df=pd.DataFrame([purchase_1,purchase_2,purchase_3],index=['store1','store2','store3'])
df


# In[7]:


df[['Name','Cost']]


# In[8]:


df.loc[:,['Name','Cost']]


# In[9]:


df.drop('store1')  #delete row


# In[10]:


copy_df=df.copy()
copy_df=copy_df.drop('store2')
df


# In[11]:


get_ipython().run_line_magic('pinfo', 'copy_df.drop')


# In[144]:


df['location']=None
df


# In[146]:


df.loc[df.index[:1], 'location'] = "shimoga"
df


# In[13]:


dir(pd)


# In[ ]:




