str1 = input("Nhập chuỗi ký tự: ")
words = str1.split()  # Tách chuỗi thành các từ bằng cách sử dụng khoảng trắng và dấu phẩy làm dấu phân cách
for word in words:
    word = word.strip(",")  # Loại bỏ dấu phẩy từ đầu và cuối của mỗi từ
    print(word)
