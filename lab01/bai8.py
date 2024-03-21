def tinh_gia_tri_bieu_thuc(x):
    # Tính giá trị của biểu thức
    y = (3*x**2 - 4*x + 1) / (2*x - 1)
    return y

def main():
    # Nhập giá trị của x từ người dùng
    x = float(input("Nhập giá trị của x: "))
    # Gọi hàm tính giá trị của biểu thức
    gia_tri = tinh_gia_tri_bieu_thuc(x)
    # Làm tròn đến số thập phân thứ hai
    gia_tri = round(gia_tri, 2)
    # In kết quả
    print("Giá trị của biểu thức là:", gia_tri)

if __name__ == "__main__":
    main()