# Nhập chuỗi ký tự từ người dùng
Str1 = input("Nhập chuỗi ký tự thứ nhất: ")
Str2 = input("Nhập chuỗi ký tự thứ hai: ")

a = 0
b = ""

for i in range(len(Str1)):
    for j in range(len(Str2)):
        c = 0
        while i + c < len(Str1) and j + c < len(Str2) and Str1[i + c] == Str2[j + c]:
            c += 1
        if c > a:
            a = c
            b = Str1[i:i + c]

print(f"Chuỗi ký tự con chung có độ dài cực đại của {Str1} và {Str2} là: {b}")
