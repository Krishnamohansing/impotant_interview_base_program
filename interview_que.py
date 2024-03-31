#print pettern
n=7
for a in range(n):
    for b in range(n//2+1):
        if a==b or a+b==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    
"""output:-
 * 
   *
     * 
       *
         *
        *
      *
    *
 *
 """
    
#print alphabet according to input  
c=int(input("Enter nu. of character:"))
n=ord('a')
while n<ord('z'):
    for _ in range(c):
        print(chr(n),end='')
        n+=1
        if n==ord('z')+1:
            break
    print()

# Print Fabinacci series in pettern
f,s=0,1
num=7
p_l=[]
for a in range(num):
    p_l.append(f)
    f,s=s,f+s
l1,l2=[],[]
for ind in range(len(p_l)):
    l1.append(p_l[ind]) if ind%2==0 else l2.append(p_l[ind])
l=l1+l2[::-1]
ind=0
for a in range(num):
    for b in range(num//2+1):
        if a==b or a+b==num-1:
            print(l[ind],end='')
        else:
            print(' ',end='')
    ind+=1
    print()
"""output:-
0
 1
  3
   8
  5
 2
1
"""

#atleast two digit is same in a number
l=[10,120]
count=0
for num in range(l[0],l[1]):
    
    if num>10:
        for ch in str(num):
            if str(num).count(ch)>1:
                count+=1
                break
            
print(count)


#quetion
num=int(input('Enter any number:'))
space=0
for lines in range(1,num+1):
    print(" "*space+str(lines))
    if lines<=num//2:
        space+=1
    else:
        space-=1
"""
output:-
1
 2
  3
   4
    5
   6
  7
 8
9
"""           