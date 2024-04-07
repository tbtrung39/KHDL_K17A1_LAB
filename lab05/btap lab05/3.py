'''3. Nhập một số tự nhiên n từ bàn phím. Viết chương trình chuyển số n từ hệ cơ số 10 sang 
nhị phân. Kết quả là chuỗi nhị phân'''
so = int(input("Nhập số tự nhiên n: "))
nhiphan = ''
while so > 0:
    nhiphan = str(so % 2) + nhiphan
    so //= 2
print("Chuyển sang nhị phân:", nhiphan)
