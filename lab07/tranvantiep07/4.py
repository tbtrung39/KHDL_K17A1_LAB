height = [161, 182, 161, 154, 176, 170, 167, 171, 170, 
          174, 150, 142, 148, 165, 170, 178, 156, 145, 
          149, 163, 162, 159, 165, 170, 180, 155, 159, 
          155, 159, 155, 153, 152, 162, 180, 168, 169, 
          168, 167, 170]
# so sinh vien : 
student = len(height)
print("so sinh vien trong nhom la : ", student)
# tinh chieu cao trung binh cua cac sinh vien trong nhom : 
sum = 0 
for i in height : 
    sum += int(i)
print("Chieu cao trung binh cua sinh vien la : ", sum/student)
# liet ke cac chieu cao khac nhau vaf trung binh chieu cao cua nhom : 
height_new = set(height)
print(height_new)

lenght_set = len(height_new)

tong = 0 
for i in height_new : 
    tong += i 
print("trung binh la : ", tong/lenght_set)