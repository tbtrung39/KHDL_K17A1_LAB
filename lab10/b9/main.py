from pk9 import in_hang_hoa,nhap_thong_tin_hang_hoa,sap_xep_theo_thue
hang_hoa = nhap_thong_tin_hang_hoa()
print("\nDanh sách hàng hóa trước khi sắp xếp:")
in_hang_hoa(hang_hoa)
hang_hoa_sau_sap_xep = sap_xep_theo_thue(hang_hoa)
print("\nDanh sách hàng hóa sau khi sắp xếp theo thứ tự giảm dần về Thuế VAT:")
in_hang_hoa(hang_hoa_sau_sap_xep)
