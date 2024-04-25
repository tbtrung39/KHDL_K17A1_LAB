a = set()
kt = int(input("Nhập số phần tử:"))
for i in range(0,kt):
    ht = int(input(f"Nhập phần tử thứ {i+1}:"))
    try:
        if ht <0:
            print("Please enter a possitive number")
            continue
        a.add(ht)
    except ValueError:
        print("Please enter a natural number")
m = set(a)
print(m)