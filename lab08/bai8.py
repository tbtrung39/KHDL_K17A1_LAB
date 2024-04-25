import math  # Thư viện toán học, cần cho giá trị của π (pi)

def tinh_chu_vi(r):
    return 2 * math.pi * r

def tinh_dien_tich(r):
    return math.pi * (r ** 2)

def main():
    r = float(input("Nhập bán kính hình tròn: "))
    chu_vi = tinh_chu_vi(r)
    dien_tich = tinh_dien_tich(r)

    print(f"Chu vi của hình tròn với bán kính {r} là: {chu_vi:.2f}")
    print(f"Diện tích của hình tròn với bán kính {r} là: {dien_tich:.2f}")

if __name__ == "__main__":
    main()