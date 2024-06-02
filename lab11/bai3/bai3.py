
with open("lab11/bai3/f_in.dat",mode="r",encoding="utf-8") as file_in:
    dayso = list(map(int,file_in.readline().strip().split(',')))
so_cuc_tri = []
dem = 0
for i in range(1,len(dayso) - 1):
       if dayso[i-1]< dayso[i]>dayso[i+1]:
              so_cuc_tri.append(dayso[i])
              dem+=1
with open("lab11/bai3/f_out.dat",mode="w") as file_out:
       chain_cuc_tri = " ".join(map(str,so_cuc_tri))
       file_out.write(str(dem)+"\n")
       file_out.write(chain_cuc_tri)
