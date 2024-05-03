def diem_trung_binh(a,b,c):
    diem_tb = (a + b + c)/3
    return diem_tb
name = input("Nhập tên sinh viên: ")
a = int(input(f"Nhập điểm toán của sinh viên {name}: "))
b = int(input(f"Nhập điểm hóa của sinh viên {name}: "))
c = int(input(f"Nhập điểm lý của sinh viên {name}: "))
diem_trung_binh(a,b,c)
print(f"Điểm trung bình của sinh viên {name} là: {diem_trung_binh(a,b,c)}")