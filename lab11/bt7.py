with open("m_num.txt", mode = "r") as m, open("n_num.txt", mode = "r") as n:
    so_m = set(map(int, m.read().split()))
    so_n = set(map(int, n.read().split()))

so_chung = so_m.intersection(so_n)

with open("so_chung.txt", mode = "w") as f:
    f.write('\n'.join(map(str, so_chung)))

with open("so_chung.txt", mode = "r") as f:
    print("Cac so chung trong ca 2 file la:")
    print(f.read())