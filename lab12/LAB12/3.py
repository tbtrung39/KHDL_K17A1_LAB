def copy_file():
    try:
        input_file_name = input("Nhập tên tập tin cần đọc: ")
        with open(input_file_name, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        with open('copy.dat', 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        
        print("Đã sao chép nội dung vào tập tin copy.dat.")
    except FileNotFoundError:
        print("Không tìm thấy tập tin với tên vừa nhập.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

copy_file()