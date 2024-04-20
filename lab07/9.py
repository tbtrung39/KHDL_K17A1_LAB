#9
n=int(input("moi nhap he tu nhien n"))
a=set()
b=()
# tao tap hop a va b
for i in range(1,n+1):
    if n%i==0:
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            a.add(i)
        elif i<n:
            b.add(i)
print("tap hop a",a)
print("tap hop b ",b)