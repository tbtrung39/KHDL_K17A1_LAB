Str1 = str(input('Nhập chuỗi 1: '))
Str2 = str(input('Nhập chuỗi 2: '))

tron_str = ''
min_length = min(len(Str1), len(Str2))

# Trộn chuỗi trong phần có độ dài nhỏ nhất
for i in range(min_length):
    tron_str += Str1[i] + Str2[i]

print("Chuỗi sau khi trộn:", tron_str)

