file_path=r'6\bang.txt'
#1,
def f1(file_path):
    print('1,Hiển thị nội dung dòng 1 và 3.')
    with open(file_path, 'r') as file:
        line = file.readlines()
        if len(line) >= 3:
            print('Dòng đầu:',line[0].strip()) #strip():Trả về một bản sao của chuỗi đã được loại bỏ khoảng trắng ở đầu và cuối.
            print('Dòng ba:',line[2].strip())
        else:
            print('File không đủ 3 dòng')
f1(file_path)

#2,
def f2(file_path):
    print('2,Hiển thị toàn bộ file')
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i,line in enumerate(lines): #truy cập cả chỉ số và giá trị trong một vòng lặp duy nhất
            print(f'Dòng {i+1}:{line.strip()}')
f2(file_path)
#3,
file_doc=r'6/bang.txt'
file_ghi=r'6/ODD.txt'
def TimSoLe(file_doc,file_ghi):
    print('3,Tìm số lẻ Ma trận 4x4')
    So=[]
    SoLe=[]
    with open(file_doc,'r') as file:
        for line in file:
            so_hang=list(map(int,line.split()))
            So.extend(so_hang)
            SoLe.extend([so for so in so_hang if so % 2 != 0])

        # Thay thế số lẻ bằng '0'
        MaTran=[]
        index=0
        for i in range(16):
            if i % 4 == 0:
                MaTran.append([])
            if index < len(SoLe) and So[i] % 2 !=0:
                MaTran[i//4].append(SoLe[index])
                index += 1
            else:
                MaTran[i//4].append(0)
        #Ghi vào ODD.txt
        with open(file_ghi,'w') as file:
            for hang in MaTran:
                file.write(' '.join(map(str,hang))+ '\n')
TimSoLe(file_doc,file_ghi)
print('Ma trận đã được lưu vào ODD.txt')        


