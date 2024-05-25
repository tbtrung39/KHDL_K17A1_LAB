import sys
sys.path.append("lab10\package_9")

import package_9

danh_sach_mat_hang = []
so_mat_hang = int(input("Nhập số lượng mặt hàng: "))
for i in range(so_mat_hang):
    mat_hang = package_9.nhap_mat_hang()
    danh_sach_mat_hang.append(mat_hang)

package_9.sap_xep_theo_thue(danh_sach_mat_hang)
package_9.hien_thi_danh_sach_mat_hang(danh_sach_mat_hang)