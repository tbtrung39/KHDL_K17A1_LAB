try:
    ngay = int(input("nhap ngay: "))
    thang = int(input("nhap thang:"))
    nam = int(input("nhap nam: "))
except ValueError as e:
    print(e)
else:
    try:
        if thang <1 or thang > 12 or ngay <1 or ngay >31:
            raise ValueError("ngay hoac thang khongg hop le")
        if thang ==1 or thang ==3 or thang  ==5 or thang == 7 or thang ==8 or thang ==10 or thang ==12:
            if ngay ==31:
                ngay=1
                if thang ==12:
                    thang = 1
                    nam+=1
                else:
                    thang +=1
            else:
                ngay +=1
        elif thang ==4 or thang == 6 or thang ==9:
            if ngay == 30:
                ngay =1
                thang+=1
            else:
                ngay +=1
        elif thang ==2:
            try:
                if(nam%4==0 and nam %100 !=0) or nam % 400 ==0:
                    assert ngay >=1 and ngay <=29,"vui long nhap lai ngay >=1 and ngay <=29"
                    if ngay ==29:
                        ngay =1
                        thang+=1
                    else:
                        ngay+=1
                else:
                    assert ngay>=1 and ngay <=28,"vui long nhap lai ngay >=1 and ngay<=28"
                    if ngay==28:
                        thang +=1
                        ngay=1
                    else:
                        ngay +=1
            except AssertionError as f:
                print(f)
        print(f"ngay ke tiep la: {ngay}/{thang}/{nam}")
    except Exception as e:
        print(e)