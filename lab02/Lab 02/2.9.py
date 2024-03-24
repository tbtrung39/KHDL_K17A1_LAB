'''
Viết chương trình cho phép nhập số KW điện tiêu thụ từ bàn phím. 
Sau đó tính tiền điện và xuất kết quả ra màn hình.
- Nếu số KW: 0 -> 100: đơn giá 2000 đồng/KW.
- Nếu số KW: 101 -> 200: đơn giá 2500 đồng/KW.
- Nếu số KW: 201 -> 300: đơn giá 3000 đồng/KW.
- Nếu số KW: > 300: đơn giá 5000 đồng/KW.
'''
# Nhập vào số KW điện tiêu thụ
so_kw_tieu_thu = float(input("Nhập vào số KW điện tiêu thụ: "))
# Xác định đơn giá dựa trên số KW
if 0 <= so_kw_tieu_thu <= 100:
    don_gia = 2000
elif 101 <= so_kw_tieu_thu <= 200:
    don_gia = 2500
elif 201 <= so_kw_tieu_thu <= 300:
    don_gia = 3000
else:
    don_gia = 5000
# Tính tiền điện
tien_dien = so_kw_tieu_thu * don_gia
# Xuất kết quả
print("Số tiền điện cần thanh toán là:", tien_dien, "đồng")
