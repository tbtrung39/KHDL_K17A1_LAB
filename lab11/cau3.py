def kiem_tra(so):
    nhi_phan = so.split(',')
    ket_qua = [b for b in nhi_phan if int(b, 2) % 5 == 0]
    return ','.join(ket_qua)

so = input("Nhập chuỗi các số nhị phân, phân tách bởi dấu phẩy: ")
ket_qua = kiem_tra(so)
print(ket_qua)