def doc_file(filename):
    with open(filename, 'r') as file:
        so = file.read().split()
    return set(map(int, so))

def ghi_so_nguyen(filename, num):
    with open(filename, 'w') as file:
        for nums in num:
            file.write(f"{nums}\n")

# Đọc file
m_nums = doc_file('b7_m_nums.txt')
n_nums = doc_file('b7_n_nums.txt')

# Tìm số chung
so_chung = m_nums.intersection(n_nums)

# Ghi số chung vào file
ghi_so_nguyen('so_chung.txt', so_chung)

print("Các số chung đã được ghi vào file so_chung.txt")
