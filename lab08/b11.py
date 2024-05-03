ho_ten=input("Họ và tên sinh viên: ")
def tinh_tb(a,b,c):
    tb=(a+b+c)/3
    return tb
a=int(input("Nhập điểm toán: "))
b=int(input("Nhập điểm hóa: "))
c=int(input("Nhập điểm lý: "))
tb=tinh_tb(a,b,c)
print(ho_ten)
print("Điểm tb 3 môn là: ",tb)