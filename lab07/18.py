dic={'23174600063':['Păn',100]}
SBD=input('nhập số báo danh:')
for i in dic.keys():
    if SBD==i:
        print('thông tin sinh viên đã tồn tại')
    else:
        HvT=input('nhập học và tên của sinh viên:')
        diem=float(input('nhập điểm của thí sinh:'))
        dic[SBD]=[HvT,diem]