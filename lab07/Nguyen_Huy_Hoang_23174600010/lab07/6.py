n=int(input())
a=[]
c=2
while len(a)<n:
   for i in range(2,c):
       if c%i==0:
           break
   else:
       a.append(c)
   c+=1
print(a)
