def  find_ucln(a,b):
    while b!=0:
        a,b = b,a%b
    return a

num_tu = int(input("Nhập tử số: "))
num_mau = int(input("Nhập mẫu số: "))
ucln = find_ucln(num_tu,num_mau)

num_mau = num_mau//ucln
num_tu = num_tu//ucln
print('phân số sau khi rút gọn là:',num_tu,'/',num_mau)