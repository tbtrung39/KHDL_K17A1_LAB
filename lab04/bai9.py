#bài 9
cac_so_nhap_vao = []
while True:
    nhap_so = int(input("số nhập vào:"))
    cac_so_nhap_vao.append(nhap_so)
    nhap_tiep = input("bạn có muốn nhập tiếp không?(y/n)")
    if nhap_tiep == "n":
        break
print(f"tổng của các số được nhập vào là:{sum(cac_so_nhap_vao)}")
