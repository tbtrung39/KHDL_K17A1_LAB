num = int(input("Nhập một số: "))
sum = 0

while num > 0:
    num_dv = num % 10  
    sum += num_dv    
    num //= 10       

print("Tổng các chữ số của số đã nhập là:", sum)
