from functools import reduce
def sum_int():
    lst = []
    n = int(input("nhập vào n từ bàn phím: "))
    for i in range(1,n+1):
        lst.append(i)
    return lst
lstcbp = sum_int()
even_n = list(filter(lambda x: x % 2 == 0, lstcbp))
sum_n = reduce(lambda x, y: x + y, even_n)
print("Tổng các số chẵn từ 1 đến n là:", sum_n)