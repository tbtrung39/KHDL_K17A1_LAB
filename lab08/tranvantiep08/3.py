def sont(n) : 
    if n < 2 : 
        return False
    else: 
        for i in range(2, n):
            if n % i == 0 : 
                return False
        return True

a = int(input("Nhap mot so : "))
for j in range(2, a):
    if sont(j) : 
        print(j) 
