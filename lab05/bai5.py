Str = input("Nhập chuỗi ký tự: ")
numbers = ''.join(filter(str.isdigit, Str))
print("Chuỗi số sau khi loại bỏ các ký tự không phải là số:", numbers)
so = int(numbers)
tong = sum(i for i in range(1, so) if so % i == 0)
if tong == so:
    print("Chuỗi số", so, "là số hoàn hảo.")
else:
    print("Chuỗi số", so, "không phải là số hoàn hảo.")
