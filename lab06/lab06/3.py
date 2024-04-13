arr = []
while True:
    num = int(input("Nhập số tự nhiên (nhập 0 để kết thúc): "))
    if num == 0:
        break
    arr.append(num)
các_số_dương = [x for x in arr if x > 0]
các_số_âm = [x for x in arr if x <= 0]
arr = các_số_dương + các_số_âm
print("Danh sách sau khi chuyển các phần tử dương lên đầu:",arr)
m = int(input("Nhập số m: "))
arr.insert(0, m)
print("Danh sách sau khi chèn số m vào đầu danh sách:",arr)
arr.append(m)
print("Danh sách sau khi chèn số m vào cuối danh sách:",arr)
if len(arr) >= 5:
    arr.insert(4, m)
    print("Danh sách sau khi chèn số m vào vị trí thứ 5:",arr)
else:
    print("Danh sách không đủ phần tử để chèn vào vị trí thứ 5.")
