print (divmod(5,2)[0])
print (pow(2,3))

a='hello word python'
b='love'
c=a.split()[0]+b+a.split()[-1]
print (c)

a='hello word python'
print (*a)
c='{1} {2} {0}'.format(*a.split())
print (c)


a=list(map(str,list(range(4))))
print (a)

a=[x*x for x in range(10) if x%2==0]
print (a)

a=list(range(5))
a.append([3,4])
print (a)

a=[1, 3, 5, 2, 4]
reversed(a)
print (a)

def summa(a,b):
    return a+b
a=summa('4','4')

def summa1(a,b):
    return a+b
a=summa1([4],[4])

print(a)

def f1(x):
    return x*x
def f2(*arr):
    return map(f1,arr)
a=list(range(5))
print (a)
#print(list(f2(a)))

a=[x*x for x in range(5)]
b={str(x):x*x for x in range(5)}
def f1(*a,**kw):
    print('args',a)
    print('kwargs',kw)

print (f1(*a))


a=[x*x for x in range(5)]
b={str(x):x*x for x in range(5)}
def f2(*a,**kw):
    print('args',a)
    print('kwargs',kw)
f2(*b)

a=[x*x for x in range(5)]
b={str(x):x*x for x in range(5)}
def f3(*a,**kw):
    print('args',a)
    print('kwargs',kw)
#f3(**a)

import os
for i in os.listdir():
    if os.path.isfile(i): print(i)
print ('next')
import os
for i in os.listdir('..'):
    print(i)



import hashlib
a='привет Питон'
h1=hashlib.md5(a.encode())
print(h1)



