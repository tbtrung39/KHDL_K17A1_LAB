nhap = input("nhập chuỗi kí tự:")
chuoi_so = ''.join(ky_tu for ky_tu in nhap if ky_tu.isdigit())
so = int(chuoi_so)
tong_uoc = sum(i for i in range (1,so) if so % i ==0)
la_so_hoan_hao = tong_uoc == so
print("chuỗi số sau khi loại bỏ kí tự không phải là số:",chuoi_so)
if la_so_hoan_hao:
    print("chuỗi này là số hoàn hảo")
else:
    print("không phải là số hoàn hảo")
    