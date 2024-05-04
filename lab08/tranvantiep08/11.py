name = input('nhap ho va ten : ')
point_math = float(input('nhap diem toan : '))
point_physics = float(input('nhap diem ly : '))
point_chemistry = float(input('nhap diem hoa : '))

def diem_tb() : 
    return (point_math + point_physics + point_chemistry) / 3

print('ten cua sinh vien la : ', name)
print('diem trung binh cac mon cua sinh vien la : ', diem_tb())