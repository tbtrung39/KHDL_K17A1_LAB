# Nhập danh sách a từ bàn phím
n = int(input("Nhập số lượng phần tử của danh sách a: "))
a = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

# Tạo danh sách b từ danh sách a, chỉ chọn những phần tử chia hết cho 3 nhưng không chia hết cho 5
b = [x for x in a if x % 3 == 0 and x % 5 != 0]
print("Danh sách b chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5:")
print(b)

# Tạo danh sách c chứa bình phương của các phần tử trong danh sách a
c = [x**2 for x in a]
print("Danh sách c chứa bình phương của các phần tử trong danh sách a:")
print(c)

# Tạo danh sách D chứa các phần tử chia hết cho 3 từ danh sách a
d = [x for x in a if x % 3 == 0]
print("Danh sách D chứa các phần tử chia hết cho 3 từ danh sách a:")
print(d)
