n = int(input("Nhập số lượng bộ ba (tên, tuổi, điểm) bạn muốn sắp xếp: "))

bo_ba = []
for i in range(n):
    ten = input(f"Nhập tên của bộ ba thứ {i+1}: ")
    tuoi = int(input(f"Nhập tuổi của bộ ba thứ {i+1}: "))
    diem = int(input(f"Nhập điểm của bộ ba thứ {i+1}: "))
    bo_ba.append((ten, tuoi, diem))

bo_ba.sort(key=lambda x: (x[0], x[1], x[2]))

print("Danh sách bộ ba sau khi sắp xếp:")
for ba in bo_ba:
    print(ba)
