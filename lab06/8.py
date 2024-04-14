n=int(input("Nhap so nguyen:"))
fibonacci=[0,1]
[fibonacci.append(fibonacci[-1] +fibonacci[-2]) for i in range(2,n)]
print(*fibonacci,sep=",")