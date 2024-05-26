import md8
kich_thuoc = int(input("Nhập kích thước của ma trận vuông: "))
matran = md8.nhap_matran_vuong(kich_thuoc)
    
print("Ma trận vừa nhập:")
md8.in_matran_vuong(matran)

md8.chuyen_vi_matran_vuong(matran)

if md8.kiem_tra_doi_xung(matran):
        print("Ma trận là ma trận đối xứng.")
else:
        print("Ma trận không phải là ma trận đối xứng.")
