sothapphan = int(input("Nhap so thap phan : "))
if sothapphan < 1 : 
    print("xin moi nhap lai !!!")
else: 
    i = ""
    while sothapphan > 0 : 
        i = str(sothapphan % 2) + i 
        sothapphan //= 2 
    print("He nhi phan duoc chuyen doi la : ", i)