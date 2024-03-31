#permutation
from itertools import permutations as p
name='abc'
for ele in p(name):
    print(''.join(ele))
    """output:-
abc
acb
bac
bca
cab
cba
    """
    
#Alternate prime
def prime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2
starting_val=int(input("Enter starting value:"))
ending_val=int(input("enter Ending value:"))
if starting_val>ending_val:
    starting_val=ending_val
count=0
while starting_val!= ending_val:
    if prime(starting_val):
        count += 1
        if count%2 != 0:
            print(starting_val)
        starting_val += 1
    else:
        starting_val += 1

#Emripnumber
def prime(num,fcount=0):
    for fa in range(1,num):
        if num%fa==0:
            fcount+=1
def reverse(num,rev=0):
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
def emrip(num):
    return reverse(num)!=num and prime(num) and prime(reverse(num))
num=int(input("enter any number"))
print('Emrip Number' if emrip(num) else 'not Emrip number') 
#pettern
m=list(map(lambda space,sv:'-'*space+''.join(list(map(str,range(sv,0,-1)))),range(4,-1,-1),range(1,6)))
print('\n'.join(m))
"""output:
----1
---21
--321
-4321
54321
"""

m=list(map(lambda space,count,num:'-'*space+str(num)*count ,range(4,-1,-1),range(1,6),range(5,0,-1)))
print('\n'.join(m))
"""
output:
----5
---44
--333
-2222
11111
"""

m=list(map(lambda space,sv:' '*space+''.join(list(map(str,range(sv,6)))),range(4,-1,-1),range(5,0,-1)))
print('\n'.join(m))
"""
output:
    5
   45
  345
 2345
12345
"""

m=list(map(lambda ev:''.join(list(map(str,range(1,ev)))),range(6,1,-1)))
print('\n'.join(m))
"""output:-
12345
1234
123
12
1
"""
#filter only prime value
l=[10,13,17,39,7,41]
f=list(filter(lambda num:len(list(filter(lambda fa:num%fa==0,range(1,num+1))))==2,l))
print(f)

#happy number by recurssin
def digSum(num):
    if num==0:
        return 0
    return (num%10)**2 + digSum(num//10)
def happy(num):
    if digSum(num) > 9:
        return happy(digSum(num))
    else:
        return digSum(num)==1 or digSum(num)==7
print(happy(88))
def happy(num):
    if num<10:
        return num
    return happy(digSum(num))==1 or happy(digSum(num))==1
print(happy(44))

#fabinacci serise
n=5
f,s=0,1
if n>0:
    for _ in range(n-1):
        f,s=s,f+s 
    print(f)
else:
    print('Not possible')
    
#using recursion
def fabi(pos):
    return pos-1 if (pos==1 or pos==2) else fabi(pos-1)+fabi(pos-2)
print(fabi(6))
#fabonacci series
n=6
a,b=0,1
while n!=0:
    print(a)
    a,b=a+b,a
    n-=1

#print only special charecter

s='we need@ t13o thi45nk& hard$'
s=s.lower()
word=''
for ch in s:
    if ch < 'a' and ch < 'z' and ch not in '0123456789':
        word+=ch
print(word)

#
n=9
for e in range(n):
    for c in range(5):
        if c==0 or c==e or e+c==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
"""
output:-
*    
**
* *
*  *
*   *
*  *
* *
**
*
"""

#suare pattern by star   
l=6
b=4
space=l-2
for n in range(0,b+1):
    if n==0 or n==b:
        print('* '*6)
    else:
        print('*  ',' '*space,' *')