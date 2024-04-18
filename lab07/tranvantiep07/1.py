while True : 
    kt = input("Nhap ky tu, nhap esc de thoat : ")
    str_new = ""
    for i in kt : 
        if not i.isdigit(): 
            str_new += i 
            kytu = set(str_new)
    if kt == "esc":
        break 
    print(kytu)
    