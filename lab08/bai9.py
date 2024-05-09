def phep_toan(a, b):
    phep_cong = a + b
    phep_tru = a - b 
    phep_nhan = a * b
    phep_chia = a / b
    return phep_cong, phep_tru, phep_nhan, phep_chia
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
ket_qua = phep_toan(a, b)
print("Kết quả phép cộng:", ket_qua[0])
print("Kết quả phép trừ:", ket_qua[1])
print("Kết quả phép nhân:", ket_qua[2])
print("Kết quả phép chia:", ket_qua[3])
