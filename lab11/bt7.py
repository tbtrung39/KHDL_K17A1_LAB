def reader(filename):
    with open(filename,'r') as file:
        so = file.read().split()
        return list(map(int,so))
def num(filename,num):
    with open(filename,'w') as file:
        file.write(f"{num}\n")
def main():
    m_nums = reader('lab11/m_num.txt')
    n_nums = reader('lab11/n_num.txt')
    if not n_nums or not m_nums:
        return
    nums = list(set(n_nums).intersection(m_nums))
    num("lab11/so_chung.txt",nums)
    print("Các số chung đã được ghi vào file so_chung.txt:")
    for i in nums:
        print(i)
main()