dien_tieu_thu=int(input("nhập số kw điện đã tiêu thụ: "))
if dien_tieu_thu>0 and dien_tieu_thu<=100:
    tien_dien=2000*dien_tieu_thu
    print(f"tiền điện {tien_dien} đồng")
elif dien_tieu_thu>100 and dien_tieu_thu<201:
    tien_dien1=(dien_tieu_thu-100)*2500+100*2000
    print(f"tiền điện {tien_dien1} đồng")
elif dien_tieu_thu>200 and dien_tieu_thu <301:
    tien_dien2=(dien_tieu_thu-200)*3000+100*2500+100*2000
    print(f"tiền điện {tien_dien2} đồng")
elif dien_tieu_thu>300:
    tien_dien3=(dien_tieu_thu-300)*5000+100*3000+100*2500+100*2000
    print(f"tiền điện {tien_dien3} đồng")