try:
    duong_dan_file1 = input("nhap path dau vao: ")
    duong_dan_file_luu = input("nhap duong dan file luu: ")
    try:
        file_nguon = open(duong_dan_file1, 'r', encoding='utf-8')
    except IOError:
        print("loi: khong mo duoc tap tin.")
        raise
    try:
        file_luu = open(duong_dan_file_luu, 'w', encoding='utf-8')
    except IOError:
        print("loi: khong mo duoc tap tin luu.")
        file_nguon.close()
        raise

    content = file_nguon.read()

    file_luu.write(content)
    print(f"noi dung da duoc luu vao {duong_dan_file_luu}")

except Exception as e:
    print(f"loi: {e}")

finally:
    try:
        file_nguon.close()
    except NameError:
        pass  
    try:
        file_luu.close()
    except NameError:
        pass 
