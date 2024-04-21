ky_tu_set = set()
print("Nhap cac ky tu , bam phim ESC de kthuc la:")
while True:
    ky_tu = input()
    if ky_tu == "":
        break
    ky_tu_set.add(ky_tu) if not ky_tu.isdigit() else None
print("Set sau khi loai bo cac ky tu so la:",ky_tu_set)