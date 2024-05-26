def Ucln(a, b):
    """Trả về ước chung lớn nhất của 2 số nguyên a, b."""
    while b:
        a, b = b, a % b
        '''
        ta gán a = b và b = a % b đến khi nào a không còn chia hết được cho b nữa thì 
        ta trả về giá trị ước chung lớn nhất cho a
        '''
    return a

def Bcnn(a, b):
    """Trả về bội số chung nhỏ nhất của 2 số nguyên a, b.
    bội chung nhỏ nhất của 2 số bằng tích 2 số a và b chia cho ước chung lớn nhất của 2 số đó
    """
    return a * b // Ucln(a, b)

def SumDivisor(n):
    divisor_sum = 0
    for i in range(1, n + 1):  # Duyệt qua tất cả các số từ 1 đến n
        if n % i == 0:  # Nếu i là ước của n
            divisor_sum += i  # Thêm i vào tổng
    return divisor_sum