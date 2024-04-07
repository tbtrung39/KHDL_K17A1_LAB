
Str = input("Nhập chuỗi ký tự: ")
a = 0
c = 1
b = ""
for i in range(len(Str) - 1):
    if Str[i] == Str[i + 1]:
        c += 1
        if c > a:
            a = c
            b = Str[i] * a
    else:
        c = 1
print("Chuỗi ký tự con có độ dài cực đại và bao gồm các phần tử giống nhau là:", b)
