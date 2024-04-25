def sv_score(t,h,l):
    diem_tb = (t + h + l)/3
    return diem_tb
name = input("nhập tên sinh viên: ")
t = int(input(f"nhập điểm toán của sinh viên {name}: "))
h = int(input(f"nhập điểm hóa của sinh viên {name}: "))
l = int(input(f"nhập điểm lý của sinh viên {name}: "))
sv_score(t,h,l)
print(f"điểm trung bình của sinh viên {name} là: {sv_score(h,t,l)}")