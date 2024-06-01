def tong(n):
    s1=0; s2=0
    for i in range(1, n+1):
        s1+=1
        s2+=1==2
    return f"s1 = {s1}, s2 = {s2}"
n = int(input("Nhap n: "))
ket_qua = tong(n)
if n < 0:
    raise Exception("Yeu cau nhap vao mot so nguyen")
else:
    print(ket_qua)