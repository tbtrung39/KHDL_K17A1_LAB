#1
n=int(input("Nhậpp số nguyên n:"))
for i in range(0,n+1):
    tong=0    
    T=2/3*(2*(i+1)/(2*i+3))
    tong+=T
    S=1+2/3+tong
print(f"Gtrị bthức = {S:.3f}")
#2
n=int(input("Nhập gtri n:"))
for i in range(1,n):
    tong=0
    for j in range(1,i):
        if i%j==0:
            tong+=j
    if tong==i:
        print(f"{i} là số hoàn hảo")
#3
n=int(input("Nhập gtri n:"))
for i in range(n,0,-1):
    for j in range(0,i):
        if j==0 or j==1:
            continue
        if i%j==0:
            break    
    else:
        print(f"{i} là số ngto")
        break
#4
n=int(input("Nhập gtri n:"))
for i in range(n,0,-1):
    for j in range(0,i):
        if j==0 or j==1:
            continue
        if i%j==0:
            break    
    else:
        print(f"{i} là số ngto")
#5
cdai=int(input("Nhập độ dài:"))
crong=int(input("Nhập độ rộng:"))
for i in range(cdai):
    for i in range(crong):
        print("*", end="")
    print()
#6
n=int(input("Nhập gtri n:"))
tong=0
for i in range(0,n+1):
    tong+=i**3
print("Tổng bậc 3 của n số đầu:",tong)
#7
n=int(input("Nhập gtri n:"))
tong=0
for i in range(1,n+1):
    tong+=1/i
print("Tổng nghịch đảo:",tong)
#8
#a
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    tong+=i
print("S1=",tong)
#b
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    if i%2==1:
       tong+=i
print("S2=",tong)
#c
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    if i%2==0:
       tong+=i
print("S3=",tong)
#9
#a
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    tong+=i**2
print("S4=",tong)
#b
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    if i%2==1:
       tong+=i**3
print("S5=",tong)
#c
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    if i%2==0:
       tong+=i**4
print("S6=",tong)
#10
n=int(input("Nhập số nguyên dương:"))
print("Dạng phân tích của",n,"là:",end=" ")
for i in range(2,n+1):
    for j in range(2,i+1):
        if i%j==0 and i==j:
           if n%i==0:
             print(i,end="")
             n//=i
        elif i%j==0:
           break   
    if n==1:    
       break
#11
    #a
n=int(input("Nhậpp cạnh tgiac:"))
for i in range(0,n):  
        if i == n - 1: 
            print('*' * (2 * n - 1))
        else:   
            print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) 
                  + ('*' if i > 0 else ''))