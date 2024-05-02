khoi_tao_set = {}
while True:
    nhap_gia_tri = input("nhập giá trị thêm vào:")
    if nhap_gia_tri == "esc":
        break
    khoi_tao_set.update({nhap_gia_tri})
print(khoi_tao_set)
