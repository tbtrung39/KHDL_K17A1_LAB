with open(file = r"lab11\bai3\f_in.dat",mode="r") as file_in:
       list_dayso = list(map(int,file_in.readline().strip().split()))
cuc_tri = []
soluong = 0
for i in range(1,len(list_dayso)):
       if list_dayso[i-1]< list_dayso[i]>list_dayso[i+1]:
              cuc_tri.append(list_dayso[i])
              soluong+=1
with open(file = r"lab11\bai3\f_out.dat",mode="w") as file_out:
       chain_cuc_tri = " ".join(map(str,cuc_tri))
       file_out.write(str(soluong)+"\n")
       file_out.write(chain_cuc_tri)