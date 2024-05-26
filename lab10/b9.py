from pk_b9 import qlyhanghoa
def in_danh_sach_hang_hoa(ds_hang_hoa):
    """In danh sách hàng hóa ra màn hình"""
    for hang_hoa in ds_hang_hoa:
        print(f"Mã hàng: {hang_hoa['ma_hang']}, Tên hàng: {hang_hoa['ten_hang']}, "
              f"Đơn vị tính: {hang_hoa['don_vi_tinh']}, Đơn giá: {hang_hoa['don_gia']}, "
              f"Số lượng: {hang_hoa['so_luong']}, Thành tiền: {hang_hoa['thanh_tien']}, "
              f"Thuế VAT: {hang_hoa['thue_vat']}")

def main():
    ds_hang_hoa = qlyhanghoa.nhap_thong_tin_hang_hoa()
    
    qlyhanghoa.tinh_thanh_tien(ds_hang_hoa)
    
    qlyhanghoa.tinh_thue_vat(ds_hang_hoa)
    
    print("Danh sách hàng hóa trước khi sắp xếp:")
    in_danh_sach_hang_hoa(ds_hang_hoa)
    
    ds_hang_hoa_sap_xep = qlyhanghoa.sap_xep_theo_thue(ds_hang_hoa)
    
    print("\nDanh sách hàng hóa sau khi sắp xếp theo thuế VAT giảm dần:")
    in_danh_sach_hang_hoa(ds_hang_hoa_sap_xep)

if __name__ == "__main__":
    main()
