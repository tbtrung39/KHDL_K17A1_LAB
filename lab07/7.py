A = set()
B = set()
while True:
    n = input("Nhập phần tử cho tập A (nhập 'done' để kết thúc): ")
    if n == 'done':
        break
    A.add(n)
while True:
    m = input("Nhập phần tử cho tập B (nhập 'done' để kết thúc): ")
    if m == 'done':
        break
    B.add(m)
phan_tu_chung = A & B
print("Các phần tử chung của A và B là: ", phan_tu_chung)