def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def kiem_tra_snt(n):
    cac_so_nguyen_to = []
    for n in range(2, n):
        if so_nguyen_to(n):
            cac_so_nguyen_to.append(n)
    return cac_so_nguyen_to
n = int(input("Nhập số nguyên dương: "))
ket_qua = kiem_tra_snt(n)
print(f"Các số nguyên tố nhỏ hơn {n} là {ket_qua}")