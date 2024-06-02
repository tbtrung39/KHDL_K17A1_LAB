with open('lab11/f_in.dat','r') as file_in:
    so = list(map(int,file_in.readline().strip().split(',')))
so_cuc_tri = []
dem = 0
for i in range(1,len(so)-1):
       if so[i-1]<so[i]>so[i+1] or so[i-1]>so[i]<so[i+1]:
              so_cuc_tri.append(so[i])
              dem+=1
with open('lab11/f_out.dat','w') as file_out:
       chain_cuc_tri = " ".join(map(str,so_cuc_tri))
       file_out.write(str(dem)+"\n")
       file_out.write(chain_cuc_tri)