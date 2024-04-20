import random
a = [random.choice([1, 2.5, 'abc']) for _ in range(10)]
so_nguyen = 0
so_thuc = 0
chuoi_ki_tu = 0
for phan_tu in a:
    if isinstance(phan_tu, int):
        so_nguyen += 1
    elif isinstance(phan_tu, float):
        so_thuc += 1
    elif isinstance(phan_tu, str):
        chuoi_ki_tu += 1
print(f"Số lượng số nguyên: {so_nguyen}")
print(f"Số lượng số thực: {so_thuc}")
print(f"Số lượng chuỗi kí tự: {chuoi_ki_tu}")