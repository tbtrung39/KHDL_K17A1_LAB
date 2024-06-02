import math
def la_nguyen_to(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def cac_uoc_nguyen_to(n):
    uoc_so = set()
    if n % 2 == 0:
        uoc_so.add(2)
        while n % 2 == 0:
            n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            if la_nguyen_to(i):
                uoc_so.add(i)
            while n % i == 0:
                n //= i
    if n > 2:
        uoc_so.add(n)
    return sorted(uoc_so)

def doc_va_xu_ly_tap_tin():
    with open('lab11/f_in.dat', 'r') as file_in:
        cac_so = [int(line.strip()) for line in file_in.readlines()]
    with open('lab11/f_out.dat', 'w') as file_out:
        for so in cac_so:
            uoc_so = cac_uoc_nguyen_to(so)
            file_out.write(' '.join(map(str, uoc_so)) + '\n')
        print(f"Dữ liệu đã được xử lý và ghi vào tệp f_out.dat.")

doc_va_xu_ly_tap_tin()
