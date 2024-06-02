def chuoi_tu(chuoi):
    tu = chuoi.split(',')
    tu.sort()
    return ','.join(tu)

chuoi = input("Nhập chuỗi các từ, phân tách bởi dấu phẩy: ")
ket_qua = chuoi_tu(chuoi)
print(ket_qua)