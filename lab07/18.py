tcdt={}
n=int(input("Nhập sô luong sinh viên:"))
for i in range(n):
    so_bao_danh=input("Nhập số báo danh:")
    ten=input("Nhập họ và tên:")
    diem=float(input("Nhập điểm:"))
    tcdt[so_bao_danh]={"tên":ten,"Điểm":diem}
a=input("Nhập sbd cần kiểm tra:")
if a in tcdt:
    ts=tcdt[a]
    print("Số báo danh của thí sinh {a}")
    print("Họ tên thí sinh {a}")
    print("Điểm của thí sinh{a}")
else:
    n_ten=str(input("Nhập tên thí sinh mới:"))
    n_diem=float(input('Nhập điểm của thí sinh mới:'))
    tcdt[a]={"name":n_ten,"diem":n_diem}

