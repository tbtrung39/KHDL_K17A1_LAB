from __pycache__ import module_qlyhanghoa
hang_hoa = module_qlyhanghoa.nhap_thong_tin_hang_hoa()
print("\nDanh sách hàng hóa trước khi sắp xếp:")
module_qlyhanghoa.in_hang_hoa(hang_hoa)
hang_hoa_sau_sap_xep = module_qlyhanghoa.sap_xep_theo_thue(hang_hoa)
print("\nDanh sách hàng hóa sau khi sắp xếp theo thứ tự giảm dần về Thuế VAT:")
module_qlyhanghoa.in_hang_hoa(hang_hoa_sau_sap_xep)