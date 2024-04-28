def UCLN(a,b):
    if b==0:
        return a
    return UCLN(b,a%b)
def rut_gon_phan_so(tu_so,mau_so):
    ucln=UCLN(tu_so,mau_so)
    x=tu_so//ucln
    y=mau_so//ucln
    print(f"Phân số tối giản:{x}/{y}")
tu_so=int(input('Nhập tử số:'))
mau_so=int(input('Nhập mẫu số:'))
rut_gon_phan_so(tu_so,mau_so)