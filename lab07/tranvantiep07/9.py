n = int(input("Nhập một số tự nhiên: "))

# Ước của n: 
set_uoc = set()
for i in range(2, n):
    if n % i == 0:
        set_uoc.add(i)
    if i * i >= n: 
        break
# tim tap A co so nguyen to la uoc cua A : 
A = set() 
for i in set_uoc:
    is_prime = True 
    for j in range(2, i): 
        if i % j == 0 : 
            is_prime = False
            break 
    if is_prime :
        A.add(i)
print("Tap A : ", A)
# tim tap B co cac so nguyen to nho hon n va khong phai uoc so cua A : 
B = set() 
for i in range(2, n ):
    if i not in set_uoc:
        is_prime = True 
        for j in range(2, i): 
            if i % j == 0 : 
                is_prime = False
                break 
        if is_prime :
            B.add(i)
print("Tap B : ", B)
