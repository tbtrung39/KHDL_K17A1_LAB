from functools import reduce
def sum_int(n):
    lst = []
    for a in range(n):
        a = int(input(f" số nguyên thứ {a +1 } : "))
        lst.append(a)
    return lst
n = int(input("Nhập n: "))
lstcbp = sum_int(n)
even_n = list(filter(lambda x: x % 2 == 0, lstcbp))
sum_n = reduce(lambda x, y: x + y, even_n)
print("Tổng các số chẵn từ 1 đến n là:", sum_n)