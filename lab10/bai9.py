
from package_9  import qlyhanghoa

def main():
    danh_sach_mat_hang = qlyhanghoa.nhap_danh_sach_mat_hang()

    print("\nDanh sách mặt hàng trước khi sắp xếp:")
    qlyhanghoa.hien_thi_danh_sach(danh_sach_mat_hang)

    danh_sach_sap_xep = qlyhanghoa.sap_xep_giam_dan_theo_thue(danh_sach_mat_hang)

    print("\nDanh sách mặt hàng sau khi sắp xếp theo thuế VAT giảm dần:")
    qlyhanghoa.hien_thi_danh_sach(danh_sach_sap_xep)

if __name__ == "__main__":
    main()