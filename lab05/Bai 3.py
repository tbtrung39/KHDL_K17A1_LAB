'''
Nhập vào một số tự nhiên n từ bàn phím. 
Viết chương trình chuyển số n từ hệ cơ số 10 sang hệ nhị phân. Kết quả là chuỗi nhị phân.
'''
chuoi = ""
n = int(input("Nhập vào số nguyên: "))
if n < 0:
    print("Nhập lại số khác")
else:
    while n > 0:
        phan_du = n % 2
        chuoi = str(phan_du) + chuoi
        n = n // 2
    print("Chuyển số từ hệ 10 sang hệ nhị phân được:", chuoi)