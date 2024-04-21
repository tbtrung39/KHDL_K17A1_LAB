thong_ke=[161,182,161,154,176,170,174,150,142,148,165,170,178,156,145,149,163,162,159,165,165,170,180,155,159,155,153,162,180,168,169,168,167,170]
soluongsv=len(thong_ke)
chieucaotrungbinh=sum(thong_ke)/soluongsv
print("Số lượng sinh viên:", soluongsv)
print("Chiều cao trung bình:", chieucaotrungbinh)
thong_ke_chi_tiet = {}
for chieucao in thong_ke:
    if chieucao in thong_ke_chi_tiet:
        thong_ke_chi_tiet[chieucao] += 1
    else:
        thong_ke_chi_tiet[chieucao] = 1
for chieucao, so_luong in thong_ke_chi_tiet.items():
    print(f"Chiều cao {chieucao} có {so_luong} sinh viên")
    chieucaotrungbinh = chieucao * so_luong / so_luong
    print(f"Chiều cao trung bình của nhóm {chieucao}: {chieucaotrungbinh}")
        