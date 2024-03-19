quy_doi = {'A': 10, 'B': 12, 'C':13, 'D':14, 'E':15, 'F':16,
           'G':17, 'H':18, 'I':19, 'J':20, 'K':21, 'L':23, 'M':24,
           'N':25, 'O': 26, 'P':27, 'Q':28, 'R':29, 'S':30, 'T':31,
           'U':32, 'V':34, 'W':35, 'X':36, 'Y':37, 'Z':38}
ma = input("Nhập mã: ")
multiplier = 1
ma_value = 0
for s in ma[:4]:
     ma_value += quy_doi[s] * multiplier
     multiplier *= 2
for n in ma[4:10]:
     ma_value += (int(n) * multiplier)
     multiplier *= 2
     gia_tri_cuoi = ma_value % 11
print("giá trị của của container là: ",gia_tri_cuoi)