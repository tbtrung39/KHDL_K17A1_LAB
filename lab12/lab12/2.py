def checkLoi():
    try:
        string= input('Nhập chuỗi kí tự:')
        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                raise Exception('Lỗi nhập lặp lại!')
            for i in range(len(string)-4):
                if len(set(string[i:i+5])) == 1:
                    raise Exception('Lỗi nhập lặp lại!')
    except Exception as e:
        print(e)
    else:
        print('Chuỗi kí tự hợp lệ!')
    finally:
        print('Kết thúc kiểm tra.')
#Gọi hàm
checkLoi()
