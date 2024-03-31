n = int(input("Nhập số lượng phần tử (n): "))
tong = 1
mau_so = 3

for i in range(1, n + 1):
    tong += (tong * i) / mau_so
    mau_so += 2

ket_qua = round(tong, 3)
print("Kết quả của phép toán là:", ket_qua)
