chuoi_nhi_phan = input("Nhập chuỗi ký tự nhị phân: ")
if not all(char in '01' for char in chuoi_nhi_phan):
    print("Chuỗi không hợp lệ. Vui lòng chỉ nhập các ký tự nhị phân (0 hoặc 1).")
else:
    so_thap_phan = int(chuoi_nhi_phan, 2)
    print("Số thập phân tương ứng của chuỗi nhị phân là:", so_thap_phan)
