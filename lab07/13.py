tu_dien_W ={}
n= input("Nhap chuoi ki tu:")
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        chuoi_con_K=n[i:j]
        if chuoi_con_K in tu_dien_W:
            tu_dien_W[chuoi_con_K] += 1
        else:
            tu_dien_W[chuoi_con_K] = 1
print("Tu dien co thanh phan con:",tu_dien_W)