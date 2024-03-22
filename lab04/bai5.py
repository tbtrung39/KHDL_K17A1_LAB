#bài 5
cac_so_duoc_nhap = []
while True:
    nhap_so = int(input("số nhập vào:"))
    if nhap_so < 0 :
        break
    else:
        cac_so_duoc_nhap.append(nhap_so)
        print(cac_so_duoc_nhap)
print(f"các số được nhập là:{cac_so_duoc_nhap}")