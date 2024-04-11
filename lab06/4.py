list = []
while True:
    nhap = int(input("nhập phần tử đã có cho đên khi nhập 0 vào để kết thúc:"))
    if nhap == 0:
        break
    list.append(nhap)
list = [1,2,3] + list + [1,2,3] 
print("danh sách sau khi chèn:")
print(list)
k = int(input("nhập phần tử k để xóa:"))
if k in list:
    list.remove(k)
list.sort()
print("danh sách sau khi tăng dần")
print(list)
list.sort(reverse=True)
print("danh sách sau khi nhập giảm dần")
print(list)