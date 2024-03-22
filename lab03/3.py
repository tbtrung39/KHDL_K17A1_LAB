n=int(input("Nhập N:"))
for i in range(n,0,-1):
      for j in range(0,i):
          if j==0 or j==1:
                continue
          if i%j==0:
                break
      else:
               print("Đây là số nguyên tố",i)