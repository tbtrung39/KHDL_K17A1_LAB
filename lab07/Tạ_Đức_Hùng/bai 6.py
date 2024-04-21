n = int(input("NHap so tu nhien : "))
#in ra man hinh day n so nguye nto dau tien :
set_new = set() 
for i in range(2, n ):
    is_prime = True 
    for j in range(2, i): 
        if i % j == 0 : 
            is_prime = False
            break 
    if is_prime :
        set_new.add(i)
print(set_new) 

