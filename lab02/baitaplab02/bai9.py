so_kwh = float(input("Enter in the kwh:"))
if 0<=so_kwh<=100:
    don_gia = so_kwh*2000
    print("tien dien la:",don_gia)
elif 101<=so_kwh<=200:
    don_gia=100*2000+(so_kwh-100)*2500
    print("tien dien la:",don_gia)
elif 201<=so_kwh<=300:
    don_gia=100*2000+200*2500+(so_kwh-200)*3000
    print("tien dien la:",don_gia)
elif so_kwh>=300:
    don_gia=100*2000+200*2500+300*3000+(so_kwh-300)*5000
    print("tien dien la:",don_gia)
else:
    print('error,please try again')