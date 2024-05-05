def permutation(n):
    if n == 1:  # Trường hợp cơ bản: n = 1
        return [[1]]  # Trả về một danh sách chứa một hoán vị đơn giản [1]

    # Gọi đệ quy để lấy tất cả các hoán vị của dãy từ 1 đến n-1
    prev_permutations = permutation(n - 1)

    # Tạo một danh sách mới để lưu trữ tất cả các hoán vị của dãy từ 1 đến n
    permutations = []

    # Duyệt qua từng hoán vị trong danh sách hoán vị của dãy từ 1 đến n-1
    for prev_perm in prev_permutations:
        # Duyệt qua từng vị trí để chèn phần tử n vào hoán vị đã có
        for i in range(n):
            # Tạo một bản sao của hoán vị trước đó
            new_perm = prev_perm[:]

            # Chèn phần tử n vào vị trí i
            new_perm.insert(i, n)

            # Thêm hoán vị mới vào danh sách hoán vị
            permutations.append(new_perm)

    return permutations

# Nhập số tự nhiên n từ người dùng
n = int(input("Nhập một số tự nhiên n: "))

# Gọi hàm và in ra tất cả các hoán vị của dãy từ 1 đến n
print("Tất cả các hoán vị của dãy từ 1 đến", n, "là:")
for perm in permutation(n):
    print(perm)
