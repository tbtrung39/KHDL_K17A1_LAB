A = []
while True:
    n = int(input("Nhap vao mot so nguyen: "))
    hoi= input("Nhap 0 de dung chuong trinh: ")
    A.append(n)
    if hoi == "0":
        break
B = [i for i in A if i%3 ==0 and i%5!= 0]
C = [i*i for i in A]
D = [i for i in A if i%3==0]
print("B la: ", B)
print("C la: ", C)
print("Dla: ", D)