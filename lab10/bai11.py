def u():
    name =  input('nhập họ tên học sinh: ')
    toan  =  int(input('nhập điểm toán : '))
    ly  =  int(input('nhập điểm lý : '))
    hoa  =  int(input('nhập điểm hoa : '))
    if toan >=0and ly>=0and hoa>=0:
        tb = (toan+ly+hoa)/3
        print('học sinh',name,' có điểm trung bình là :',tb)
    else:
        print('điểm phải lớn hơn 0 ')
    return

u()


