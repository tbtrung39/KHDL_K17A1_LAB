ban_kinh=float(input("Nhập bán kính r: "))
chieu_cao=float(input("nhập chiều cao h: "))
pi=3.14
dien_tich_xq_hinh_tru=2*pi*ban_kinh*chieu_cao

print(f"diện tích xung quanh hình trụ= {dien_tich_xq_hinh_tru:.2f}")

dien_tich_tp_hinh_tru=dien_tich_xq_hinh_tru + 2*pi*(ban_kinh**2)

print(f"là diện tích toàn phần hình trụ= {dien_tich_tp_hinh_tru:.2f}")

the_tich_hinh_tru=pi*(ban_kinh**2)*chieu_cao

print(f"là thể tích hình trụ= {the_tich_hinh_tru:.2f}")