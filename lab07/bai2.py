n=int(input('so tu nhien muon nhap: '))
numbers=[]
for i in range(1,n+1):
    so=int(input("nhap so tu nhien: "))
    numbers.append(so)
print(numbers)
A=set(numbers)
print(A)