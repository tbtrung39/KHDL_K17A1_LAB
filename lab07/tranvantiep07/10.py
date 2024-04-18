m = set(input("Nhap so tu nhien m : "))
n = set(input("Nhap so tu nhien n : "))
genaral = m.intersection(n)

sum = 0 
for i in genaral : 
    sum += int(i) 

print("tong cua genaral m va n la : ", sum)