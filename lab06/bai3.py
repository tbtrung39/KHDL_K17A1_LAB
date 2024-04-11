danh_sach = []
while True:
    n = int(input("nhập vào chuỗi một số nhập 0 để kết thúc: "))
    if n == 0:
        break
    danh_sach.append(n)
print(f"danh sách sau khi kết thúc chương trình {danh_sach}")
a = sorted(danh_sach,reverse=True)
print(f"danh sách sau khi chuyển các số dương lên đầu {a}")
m = int(input("nhập một số m: "))
danh_sach.append(m)
danh_sach.insert(0,m)
danh_sach.insert(5,m)
print(f"danh sách mới sau khi thêm {danh_sach}")