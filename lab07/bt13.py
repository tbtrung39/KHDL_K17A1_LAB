dict_W = {}
n = input("Nhập chuỗi kí tự: ")
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        chuoi_con = n[i:j]
        if chuoi_con in dict_W:
            dict_W[chuoi_con] += 1
        else:
            dict_W[chuoi_con] = 1
print("Từ điển có các thành phần con: ",dict_W)