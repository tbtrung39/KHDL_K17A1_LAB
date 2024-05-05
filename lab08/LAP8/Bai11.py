ten=input('Nhập tên:')
def tinh_dtb():
    t=float(input('Nhập điểm toán:'))
    l=float(input('Nhập điểm lý:'))
    h=float(input('Nhập điểm hóa:'))
    dtb=(t+l+h)/3
    return dtb
diem_tb=tinh_dtb()
print(f'Điểm trung bình ba môn :{diem_tb}')