try:
    str = input("nhap chuoi ki tu: ")
    if str.isdigit() or str.isnumeric():
                 raise ValueError("loi")
    for i in range(len(str)):
        if i<len(str)-4:
            if (str[i]*4 == str[i+1:i+5]):
                raise ValueError("loi")
    for i in range(len(str)):
        if i<len(str)-2:
            if str[i]*3 ==str[i+1:i+4]:
                raise ValueError("vui long nhap lai")
    for i in range(len(str)):
        if i<len(str)-1:
            if str[i]==str[i+1] :
                raise ValueError("loi")
except ValueError as e:
       print("Error:",e)
else:
       print("chuong trinh tiep tuc hoat dong") 

