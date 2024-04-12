'''
12. Giá sử là dữ liệu được người dùng nhập vào từ giao diện điều khiển. Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện điều khiển.
Định dạng nhật ký được hiển thị như sau:
D 100
W 200
(D là tiền gửi, W là tiên rút ra).
Giả sử đầu vào được cung cấp là:
D 300
D 300
W 200
D 100
Thì đầu ra sẽ là:
500
'''
def tinh_so_tien_thuc(nhat_ky):
    so_tien_thuc = 0
    for giao_dich in nhat_ky:
        loai, so_tien = giao_dich
        if loai == 'D':
            so_tien_thuc += int(so_tien)
        elif loai == 'W':
            so_tien_thuc -= int(so_tien)
    return so_tien_thuc

def main():
    nhat_ky = []
    print("Nhập nhật ký giao dịch:")
    while True:
        giao_dich = input().split()
        if not giao_dich:
            break
        nhat_ky.append(giao_dich)
    
    so_tien_thuc = tinh_so_tien_thuc(nhat_ky)
    print("Số tiền thực của tài khoản là:", so_tien_thuc)

if __name__ == "__main__":
    main()
