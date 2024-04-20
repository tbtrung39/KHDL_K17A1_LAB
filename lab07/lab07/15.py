list1 = [int(x) for x in input("Nhập danh sách số (phân tách bằng khoảng trắng): ").split()]
list2 = input("Nhập danh sách tên (phân tách bằng khoảng trắng): ").split()
dictionary = {a: ten for a, ten in zip(list1, list2)}
print("Từ điển được tạo:")
print(dictionary)
