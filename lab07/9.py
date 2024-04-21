n=int(input("nhập một số tự nhiên n : "))
A={i for i in range(1,n+1) if n%i==0 and all ( i % j !=0 for j in range(2, int(i**0.5)+1))}
B={i for i in range(2,n) if all (n%i != 0 for j in range(2, int(i**0.5)+1))}
print("tập hợp A ",A)
print("tập hợp B ",B)
