#Bài 1
def Sum1(n):
    if n < 1:
        raise ValueError('Giá trị n là số nguyên dương')
    if n == 1:
        return 1
    return n + Sum1(n-1)

def Sum2(n):
    if n < 1:
        raise ValueError('Giá trị n là số nguyên dương')
    if n == 1 :
        return 1
    return n**2 + Sum2(n-1)

try:
    n = int(input('Nhập giá trị:'))
    if n <= 0:
        raise ValueError('Giá trị n là số nguyên dương')
    s1=Sum1(n)
    s2=Sum2(n)
    print(f'Tổng của S1 là : {s1}')
    print(f'Tổng của S2 là : {s2}')
except ValueError as a:
    print(f'Giá trị nhập vào không hợp lệ {a}')