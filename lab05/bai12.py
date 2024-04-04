a = input("Nhập chuỗi số a: ")
b = input('Nhập chuỗi số b: ')
for i in range(1 , len(a)):
    for j in range(1, len(b)):
        A = (a[:i])
        B = (a[i:])
        C = (b[:j])
        D = (b[i:])
if int(A) + int(B) == int(C) + int(D):
    print(f"{A} + {B} = {C} + {D}")
else:
    print("Không tồn tại cách đặt")

