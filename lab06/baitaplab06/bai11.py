n = int(input("Nhập số lượng phần tử của danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i + 1} của danh sách A: ")) for i in range(n)]
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5:")
print(B)