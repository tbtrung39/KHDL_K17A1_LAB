try:
       a = int(input("nhap a: "))
       b = int(input("Nhap b: "))
       c = int(input("Nhap c: "))
       if str(a).isalpha() or str(b).isalpha() or str(c).isalpha():
              raise ValueError("loi ky tu")
       elif a<=0 or b<=0 or c<=0:
              raise ValueError("loi nho hon hoac bang 0")
       elif a+b<c or a+c<b or c+b<a:
              raise ValueError("ba canh khong phai tam giac")
except ValueError as e:
       print(e)
else:
       print("khong co loi nao xuat hien")
    