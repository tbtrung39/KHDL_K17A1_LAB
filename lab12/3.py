try:
    ten_file = input("Nhập tên tập tin cần đọc: ")
    with open(ten_file, 'r', encoding='utf-8') as infile:
        noi_dung = infile.read()

    with open('copy.dat', 'w', encoding='utf-8') as outfile:
        outfile.write(noi_dung)

    print("Nội dung file ở copy.dat.")
except FileNotFoundError:
        print("Không tổn tại")
except Exception as e:
        print("Lỗi không xác định")