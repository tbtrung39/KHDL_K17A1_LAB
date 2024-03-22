x = float(input("Nhập số lượng gam Al2O3: "))
y = float(input("Nhập nồng độ mol/lit của dung dịch NaOH: "))
z = float(input("Nhập nồng độ mol/lit của dung dịch HCl: "))
n_Al2O3 = x / 101.96 
n_NaOH = 0.1 * y 
n_HCl = 0.1 * z  
if n_Al2O3 > n_NaOH:
    print("Sau phản ứng có kết tủa")
    if n_NaOH > n_HCl:
        print("Sau khi thêm HCl, có dung dịch trong")
    else:
        print("Sau khi thêm HCl, không có dung dịch trong")
else:
    print("Sau phản ứng không có kết tủa")