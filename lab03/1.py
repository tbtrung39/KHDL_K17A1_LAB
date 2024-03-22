n=int(input("Nhập  số N:"))
t1=1
ket_qua=1
for i in range(0,n+1):
    t1*=(2*(i+1))(2*i+3)
    ket_qua+=t1
    print("Tổng=",ket_qua)