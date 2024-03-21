days= int(input("nhap so ngay trong thang: "))
month=int(input("nhap so thang: "))

if month <1 and month >12:
    print("vui long nhap lai so thang")
else:
    if month ==1:
        if days >= 1 and days <=30:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days ==31:
            print("ngay tiep theo la 1 thang 2")
        else:
            print("vui long nhap lai days")
    elif month ==2:
        if days >=1 and days <= 27:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days == 28:
            print("ngay tiep theo la 1 thang 3")
        else:
            print("vui long nhap lai days")
    elif month ==3:
        if days >=1 and days <= 30:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days == 31:
            print("ngay tiep theo la 1 thang 4")
        else:
            print("vui long nhap lai days")
    elif month ==4:
        if days >=1 and days <=  29:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days == 30:
            print("ngay tiep theo la 1 thang 5")
        else:
            print("vui long nhap lai days")
    elif month ==5:
        if days >=1 and days <= 30:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days == 31:
            print("ngay tiep theo la 1 thang 6")
        else:
            print("vui long nhap lai days")
    elif month ==6:
        if days >=1 and days <= 29:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days == 30:
            print("ngay tiep theo la 1 thang 7")
        else:
            print("vui long nhap lai days")
    elif month ==7:
        if days >=1 and days <= 30:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days == 31:
            print("ngay tiep theo la 1 thang 8")
        else:
            print("vui long nhap lai days")
    elif month ==8:
        if days >=1 and days <= 30:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days == 31:
            print("ngay tiep theo la 1 thang 9")
        else:
            print("vui long nhap lai days")
    elif month ==9:
        if days >=1 and days <= 29:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days == 30:
            print("ngay tiep theo la 1 thang 10")
        else:
            print("vui long nhap lai days")
    elif month ==10:
        if days >=1 and days <= 30:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days == 31:
            print("ngay tiep theo la 1 thang 11")
        else:
            print("vui long nhap lai days")
    elif month ==11:
        if days >=1 and days <= 29:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days == 30:
            print("ngay tiep theo la 1 thang 12")
        else:
            print("vui long nhap lai days")
    elif month ==12:
        if days >=1 and days <= 30:
            days+=1
            print("ngay tiep theo la {} thang {}".format(days,month))
        elif days == 31:
            print("ngay tiep theo la 1 thang 1 cua nam sau")
        else:
            print("vui long nhap lai days")