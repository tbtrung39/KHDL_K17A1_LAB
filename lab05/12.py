a = input("nhap chuoi so a:")
b = input("nhap chuoi so b:")
for i in range(1, len(a)):
    for j in range(1, len(b)):
        A = (a[:1])
        B = (a[1:])
        C = (b[:j])
        D = (b[i:])
        if int(A) + int(B) == int(C) + int(D):
            print(f"{A} + {B} = {C} + {D}")
        else:
            print("khong ton tai cai dat")