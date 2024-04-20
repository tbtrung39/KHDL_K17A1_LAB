a = set()
while True:
    element = input("Nhập các phần tử (Nhập để kết thúc): ")
    if element == "":
        break
    a.add(element)
so_nguyen = sum(n.isdigit() for n in a)
so_thuc = sum('.' in n and n.replace('.', '', 1).isdigit() for n in a)
so_ky_tu = len(a) - so_nguyen - so_thuc
print(f"Số nguyên: {so_nguyen}")
print(f"Số thực: {so_thuc}")
print(f"Số ký tự: {so_ky_tu}")
