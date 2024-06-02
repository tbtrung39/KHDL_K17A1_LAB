def doc_file (filename):
    with open (filename,'r') as file:
        so = file.read().split()
        return set(map(int,so))
def ghi_so_nguyen(filename,num):
    with open (filename,'w') as file:
        for nums in num:
            file.write(f"{nums}\n")
#doc file
m_nums = doc_file('b7_m_nums.txt')
n_nums = doc_file('b7_n_nums.txt')
so_chung = m_nums.intersection(n_nums)
ghi_so_nguyen('so_chung.txt',so_chung)
print("Cac so chung da dc ghi vao file so_chung.txt")