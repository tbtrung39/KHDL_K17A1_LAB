while True :  
    n = float(input("Nhap so can doi : "))
    chu = []
    for i in str(n): 
        if i == "1" : 
            chu.append("một")
        elif i == "2": 
            chu.append("hai")
        elif i == "3": 
            chu.append("ba")
        elif i == "4": 
            chu.append("bốn")
        elif i == "5": 
            chu.append("năm")
        elif i == "6": 
            chu.append("sáu")
        elif i == "7": 
            chu.append("bảy")
        elif i == "8": 
            chu.append("tám")
        elif i == "9":
            chu.append("chín")
        elif i == ".": 
            chu.append("phẩy")
        else: 
            chu.append("không")
    print("chu so ma ban chon đc la : ", " ".join(chu))
    break


