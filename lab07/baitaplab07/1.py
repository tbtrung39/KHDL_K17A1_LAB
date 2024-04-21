a = set()
while True:
    kt = input("Nhập các phần tử:")
    if kt == "ESC":
        break
    if kt.isalpha():
        a.add(kt)
print(a)
