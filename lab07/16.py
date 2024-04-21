list = [1, 2, 3, 2, 4]
chi_so = {}
for j in range(len(list)):
    num = list[j]
    if num + 1 in chi_so:
        print(f"Cặp chỉ số thỏa mãn: ({chi_so[num+1]}, {j})")
    chi_so[num] = j
