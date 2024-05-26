import package_9.qlyhanghoa as qlyhanghoa

def main():
    x =  int(input('nhập sô lượng hàng hóa ở đây: '))
    hang_hoa_list = []
    for _ in range(x):
        item = qlyhanghoa.nhap_thong_tin()
        item['tien'] = qlyhanghoa.tinh_tien(item['dongia'], item['soluong'])
        item['thue'] = qlyhanghoa.tinh_thue(item['tien'])
        hang_hoa_list.append(item)

    sorted_hang_hoa = qlyhanghoa.sap_xep_hang_hoa(hang_hoa_list)
    for item in sorted_hang_hoa:
        print(f"Mã hàng: {item['mahang']}, Tên hàng: {item['tenhang']}, Đơn vị tính: {item['donvitinh']}, "
              f"Đơn giá: {item['dongia']}, Số lượng: {item['soluong']}, Thành tiền: {item['tien']}, Thuế VAT: {item['thue']}")

main()
