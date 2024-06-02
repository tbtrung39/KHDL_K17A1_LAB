def tu_dien(n):
    return {i: i * i for i in range(1, n + 1)}

n = int(input("Nhập số nguyên n: "))
ket_qua = tu_dien(n)
print(ket_qua)