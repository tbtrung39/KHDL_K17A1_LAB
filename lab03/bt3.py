n= int(input('Nhập số cần kiểm tra:'))

for i in range(2,n):
    if n % i ==0:
        print(f'{n} không là số nguyên tố')
    break
