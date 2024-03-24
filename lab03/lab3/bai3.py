
n = int(input("Nhập một số nguyên dương n: "))
#kiem tra snt
la_so_nguyen_to=True

if n < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_so_nguyen_to = False
            break
        
if la_so_nguyen_to:
    print (f"{n} la so nguyen to.")
else:
    # Tim so nguyen to gan nhat
    so_nguyen_to_be_hon= n - 1
    so_nguyen_to_lon_hon= n + 1

    while True:
        la_so_nguyen_to_be_hon = True
        la_so_nguyen_to_lon_hon = True
        
        if so_nguyen_to_be_hon < 2:
            la_so_nguyen_to_be_hon = False
        else:
            for i in range(2, int(so_nguyen_to_be_hon**0.5) + 1):
                if so_nguyen_to_be_hon % i == 0:
                    la_so_nguyen_to_be_hon = False
                    break
            
        if so_nguyen_to_lon_hon < 2:
            la_so_nguyen_to_lon_hon = False
        else:
            for i in range(2, int(so_nguyen_to_lon_hon**0.5) + 1):
                if so_nguyen_to_lon_hon % i == 0:
                    la_so_nguyen_to_lon_hon = False
                    break
                
        if la_so_nguyen_to_be_hon:
            print(n, "không phải là số nguyên tố. Số nguyên tố gần nhất là:", so_nguyen_to_be_hon)
            break
        elif la_so_nguyen_to_lon_hon:
            print(n, "không phải là số nguyên tố. Số nguyên tố gần nhất là:", so_nguyen_to_lon_hon)
            break
            
        so_nguyen_to_be_hon -= 1
        so_nguyen_to_lon_hon += 1