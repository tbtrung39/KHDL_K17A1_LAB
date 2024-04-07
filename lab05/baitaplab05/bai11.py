Str1 = "Chuỗi ký tự này, là một ví dụ. Về cách xử lý chuỗi."
Str1 = Str1.replace(',', ' ')
words = Str1.split()
print("Các từ trong chuỗi:")
for word in words:
    print(word)