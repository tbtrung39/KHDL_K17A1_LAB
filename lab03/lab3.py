#1
n=int(input("Nhập vào n:"))
t1 = 1
result=1
for i in range(0,n+1):
    t1*=(2*(i+1))/(2*i+3)
    result+=t1
print(f"Tổng chuỗi là {result}")
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
n= int(input("Nhập vào số n:"))
for so in range(2,n+1):
    flag = True
    for i in range(2,int(so**0.5)+1):
        if so % i == 0:
            flag=False
            break
    if flag:
       print("Số nguyên tố là :",so)   
#5
cdai=3
crong=5
for i in range(cdai):
    for i in range(crong):
        print("*", end="")
    print()
#6
n=int(input("Nhập gtri n:"))
if n<0:
    print("Vui lòng nhập số nguyên dương")
else:
   tong=0
   for i in range(1,n+1):
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
#a)
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    tong+=i**2
print("S4=",tong)
#b)
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    if i%2==1:
       tong+=i**3
print("S5=",tong)
#c)
n=int(input("Nhập gtri n:"))
tong=0
if n<=0:
    print("Kết thúc!")
for i in range(0,n+1):
    if i%2==0:
       tong+=i**4
print("S6=",tong)
#10
n = int(input("nhap vao mot so nguyen duong: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    i = 2
    lst = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            lst.append(i)
    if n > 1:
        lst.append(n)

    print("Dạng phân tích thừa số nguyên tố của", n, "là:", lst)
#11
check_digit = input("Nhập mã số kiểm tra: ")
values = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}
S = 0
sum=0
for i in range(len(check_digit[:4])):
        S = values[check_digit[i]]
        sum +=S*(2**i)
for i in range(len(check_digit[4:])):
        A=int(check_digit[i+4])
        sum+=A*(2**(i+4))

so_kiem_tra=sum%11
print(f"vay so kiem tra cua ma container {check_digit} la:",so_kiem_tra)