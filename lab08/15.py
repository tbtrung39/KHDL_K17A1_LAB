def tao_list(n):
    so_nguyen = []
    for i in range(n):
        n= int(input(f"Nhập số thứ {i+1}: "))
        so_nguyen.append(n)
    return so_nguyen
n = int(input("Nhập số lượng phần tử trong list: "))
list = tao_list(n)
print(list)
list2 = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0,list)))
print("Danh sách bình phương các số lẻ:", list2)