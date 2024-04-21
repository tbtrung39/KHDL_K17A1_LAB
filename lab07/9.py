n=int(input("Nhap so tu nhien:"))
#Tap hop A la uoc cua n
a=set()
for i in range (1,n):
    if n%i==0:
        a.add(i)
    else:
        so_nguyen_to=set()
        for j in range(2,n):
            la_so_nguyen_to=True
            for k in range(2,int(j**0.5)+1):
                if j%k==0:
                    la_so_nguyen_to=False
                    break
            if la_so_nguyen_to:
                so_nguyen_to.add(j)

#Tap hop B la so nguyen to va khong thuoc A
b=so_nguyen_to-a
print("Tap hop A:",a)

print("Tap hop B:",b)
