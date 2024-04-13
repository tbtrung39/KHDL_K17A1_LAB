n=int(input("moi nhap he so n:"))
fibonacci=[0 if x==0 else 1 if x==1 else fibonacci[x-1]+fibonacci[x-2] for x in range(n)]
print("day fibonacci voi" ,n, "so la:, end=")
print(* fibonacci,sep=",")