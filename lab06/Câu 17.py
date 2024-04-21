'''
Viết chương trình sinh dãy (list)A là biểu diễn của ma trận đơn vị. 
Chương trình nhập số n từ bàn phím và sinh ra ma trận đơn vị bậc n, sau đó hiện kết quả trên màn hình.
'''
# Nhập số n từ bàn phím
n = int(input("Nhập vào số n: "))

# Tạo ma trận đơn vị bậc n sử dụng tuple comprehension
ma_tran_don_vi = tuple((1 if i == j else 0 for j in range(n)) for i in range(n))

# Hiển thị ma trận đơn vị
print("Ma trận đơn vị bậc", n, "là:")
for row in ma_tran_don_vi:
    print(row)
