n = int(input("Nhap so luong phan tu cua danh sach N: "))
list_N = []
print("Nhap cac phan tu cua danh sach N:")
for i in range(n):
    num = int(input())
    list_N.append(num)

set_A = set(list_N)
print("Tap hop A duoc tao tu danh sach N la:", set_A)