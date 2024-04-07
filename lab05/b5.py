chuoi_ky_tu = input("Nhập chuỗi ký tự: ")

chuoi_so = ""
for ki_tu in chuoi_ky_tu:
    if ki_tu.isdigit():
        chuoi_so += ki_tu

print("Chuỗi ký tự chỉ chứa số:", chuoi_so)

if chuoi_so:
    so = int(chuoi_so)

    # Kiểm tra xem số có phải là số hoàn hảo không
    tong_uoc = 0
    for i in range(1, so):
        if so % i == 0:
            tong_uoc += i

    if tong_uoc == so:
        print("Chuỗi số này là số hoàn hảo.")
    else:
        print("Chuỗi số này không phải là số hoàn hảo.")
else:
    print("Không có số nào trong chuỗi đã nhập.")
