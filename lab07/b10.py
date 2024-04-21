m = int(input("Nhap so tu nhien m la:"))
n = int(input("Nhap so tu nhien n la:"))
m_str = str(m)
n_str = str(n)
chung = set()
for i in m_str:
    if i in n_str:
        chung.add(int(i))
tong_chung = sum(chung)
print("Tong cac chu so chung cua m va n la:",tong_chung)