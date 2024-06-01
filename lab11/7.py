def read_n(f):
    try:
        with open(f, 'r') as file:
            num = file.read().split()
            return list(map(int, num))
    except FileNotFoundError:
        print("ko thay tep")
        return []
    except ValueError:
        print("ko co data")
        return []

def w_num(f, num):
    with open(f, 'w') as file:
        for n in num:
            file.write(f"{n}\n")

def main():
    n_num = read_n("n.txt")
    m_num = read_n("m.txt")
    
    if not n_num or not m_num:
        return
    
    com_num = list(set(n_num).intersection(m_num))
    w_num("so_chung.txt", com_num)
    print("cac so chung la:")
    for nb in com_num:
        print(nb)

main()
