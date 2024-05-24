from hinhoc import my_Triange,my_square
# my_Triange
def main():
    a=int(input("moi nhap he so a:"))
    b=int(input("moi nhap he so b:"))
    c=int(input("moi nhap he so c:"))

    s_tam_giac=my_Triange.tinh_dien_tich(a,b,c)
    chu_vi=my_Triange.chu_vi(a,b,c)
    print(f"dien tich tam giac la:{s_tam_giac}")
    print(f"chu vi tam giac la{chu_vi}") 

# my_square

canh=float(input("moi nhap he so canh :"))
s_hinh_vuong=my_square.tinh_dien_tich_hv(canh)
chu_vi_hv=my_square.chu_vi_hv(canh)
print(f"dien tich hih vuong la:{s_hinh_vuong}")
print(f"chu vi hinh vuong la:{chu_vi_hv}")

if __name__=="__main__":
    main()


