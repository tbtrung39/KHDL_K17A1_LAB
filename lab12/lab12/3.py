def copyFile():
    try:
        fileName= input('Nhập tên tệp cần đọc:')
        with open(fileName,'r',encoding='utf-8') as file:
            content=file.read()
        with open('copy.dat','w',encoding='utf-8') as outFile:
            outFile.write(content)

        print('Đã sao chép nội dung vào tập tin copy.dat')
    except FileNotFoundError:
        print('Không tìm thấy tập tin mới nhập')
    except Exception as e:
        print(f'Lỗi xảy ra khi sap chép: {e}')
copyFile()
    