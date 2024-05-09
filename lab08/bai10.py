
def uoc_chung(a, b):
    uoc = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            uoc.append(i)
    if len(uoc) == 0:
        print("Không có ước chung của a và b")
    else:
        print(f"Các ước chung của {a} và {b} là: {uoc}")
    return uoc
a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
uoc_chung(a, b)