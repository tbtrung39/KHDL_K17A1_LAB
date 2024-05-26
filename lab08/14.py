def tao_list(n):
    so_nguyen = []
    for i in range(n):
        n= int(input(f"Nhập số thứ {i+1}: "))
        so_nguyen.append(n)
    return so_nguyen
n = int(input("Nhập số lượng phần tử trong list: "))
list = tao_list(n)
print(list)
print("Danh sách gốc:",list)
list2 = list(map(lambda x: x**2, list))
print("Danh sách bình phương:", list2)