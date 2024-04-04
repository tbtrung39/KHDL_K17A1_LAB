Str = input("Nhập chuỗi ký tự: ")
a = ""
b = Str[0]
for i in range(1, len(Str)):
    if Str[i] == Str[i - 1]:
        b += Str[i]
    else:
        if len(b) > len(a):
            a = b
        b = Str[i]
if len(b) > len(a):
    a = b
print(f"Chuỗi ký tự con có độ dài cực đại và bao gồm các phần tử giống nhau của chuỗi ký tự là: {a}")
