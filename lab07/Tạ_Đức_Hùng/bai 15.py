list1 = [1, 2, 3, 4, 5]
list2 = ['ten0', 'ten1', 'ten2', 'ten3', 'ten4']

# Kiểm tra xem hai danh sách có cùng độ dài không
if len(list1) != len(list2):
    print("Hai danh sách phải có cùng độ dài.")
else:
    # Tạo từ điển từ hai danh sách
    tu_dien = {}
    for i in range(len(list1)):
        tu_dien[f"<{list1[i]}>"] = f"<{list2[i]}>"

    # In ra ni dung của từ điển
    print("Nội dung của từ điển:")
    for key, value in tu_dien.items():
        print(f"{key}: {value}")