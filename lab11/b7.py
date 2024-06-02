import os
def doc_file(file1, file2):
    set1 = set()
    set2 = set()
    if os.path.exists(file1):
        with open(file1, 'r') as tap_tin1:
            set1 = set(map(int, tap_tin1.readlines()))
    else:
        print(f"Tệp {file1} không tồn tại.")
    
    if os.path.exists(file2):
        with open(file2, 'r') as tap_tin2:
            set2 = set(map(int, tap_tin2.readlines()))
    else:
        print(f"Tệp {file2} không tồn tại.")
    
    return set1, set2

def tim_so_chung(file1, file2, ten_tap_tin_ket_qua):
    set1, set2 = doc_file(file1, file2)
    so_chung = set1.intersection(set2)
    with open(ten_tap_tin_ket_qua, 'w') as tap_tin_ket_qua:
        for so in sorted(so_chung):
            tap_tin_ket_qua.write(f"{so}\n")
    return so_chung

file1 = "m_nums.txt"
file2 = "n_nums.txt"
ten_tap_tin_ket_qua = "so_chung.txt"

so_chung = tim_so_chung(file1, file2, ten_tap_tin_ket_qua)
print("Các số chung trong cả hai tệp là:")
for so in so_chung:
    print(so)
