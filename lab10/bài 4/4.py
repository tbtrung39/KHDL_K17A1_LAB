import giai_phuong_trinh

print("Chọn chức năng:")
print("1. Giải phương trình bậc nhất")
print("2. Giải phương trình bậc hai")

choice = int(input("Nhập lựa chọn (1/2): "))

if choice == 1:
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    result = giai_phuong_trinh.giai_pt_bac_nhat(a, b)
    print(f"Nghiệm của phương trình bậc nhất là: {result}")
elif choice == 2:
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    result = giai_phuong_trinh.giai_pt_bac_hai(a, b, c)
    if isinstance(result, tuple):
        print(f"Nghiệm của phương trình bậc hai là: x1 = {result[0]}, x2 = {result[1]}")
    else:
        print(f"Nghiệm của phương trình bậc hai là: {result}")
else:
    print("Lựa chọn không hợp lệ")