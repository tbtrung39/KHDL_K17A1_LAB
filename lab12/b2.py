try:
    str = input("nhap chuoi ki tu: ")
    if str.isdigit() or str.isnumeric():
                 raise ValueError("loi ki tu!!!")
    for i in range(len(str)):
        if i<len(str)-4:
            if (str[i]*4 == str[i+1:i+5]):
                raise ValueError("loi nhap lieu!!!")
    for i in range(len(str)):
        if i<len(str)-2:
            if str[i]*3 ==str[i+1:i+4]:
                raise ValueError("loi nhap lap lai!!!")
    for i in range(len(str)):
        if i<len(str)-1:
            if str[i]==str[i+1] :
                raise ValueError("loi nhap trung lap")
except ValueError as er:
       print("Error:",er)
finally:
       print("chuong trinh tiep tuc hoat dong")    