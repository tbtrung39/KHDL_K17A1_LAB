w = input("Nhập chuỗi ký tự w: ")
a = {}
for i in range(len(w)):
    for j in range(i+1, len(w)+1):
        b = w[i:j]
        if b in a:
            a[b] += 1
        else:
            a[b] = 1

print(a)