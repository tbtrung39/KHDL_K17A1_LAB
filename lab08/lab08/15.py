n = int(input("Nhập số lượng phần tử của list: "))
lst = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(phan_tu)
list_binh_phuong_le = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, lst)))
print("List ban đầu:", lst)
print("List chứa bình phương của các số lẻ:", list_binh_phuong_le)
