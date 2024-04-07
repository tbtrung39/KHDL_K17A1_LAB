#Nhap xau 1 va xau 2
str_1=str(input("Nhap chuoi ki tu 1:"))
str_2=str(input("Nhap chuoi ki tu 2:"))

a= len(str_1)
b= len(str_2)
#Khoi tao ma tran kich thuoc (a+1)x(b+1)
ma_tran = [[0]*(b+1) for _ in range(a+1)]
max_len=0
vi_tri_cuoi=0

for i in range(1,a+1):
    for j in range(b+1):
        if str_1[i-1] == str_2[j-1]:
            ma_tran[i][j] = ma_tran[i-1][j-1] +1
            if ma_tran[i][j] > max_len:
                max_len = ma_tran[i][j]
                vi_tri_cuoi = i
            else:
                ma_tran[i][j] = 0

max_chuoi_con_chung= str_1[vi_tri_cuoi-max_len:vi_tri_cuoi]

if max_len>0:
    print("Chuoi con chung co do dai cuc dai la:", max_chuoi_con_chung)
else:
    print("Khong co chuoi con chung")