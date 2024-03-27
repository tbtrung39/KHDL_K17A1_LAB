n = int(input("Nhập một số nguyên dương n: "))

if n <= 0:
    print("n phải là số nguyên dương. Chương trình đã dừng.")
else:
    S1 = sum(range(1, n + 1))
    S2 = sum(range(1, 2 * n + 2, 2))
    S3 = sum(range(2, 2 * n + 1, 2))

    print("a) S1 =", S1)
    print("b) S2 =", S2)
    print("c) S3 =", S3)
