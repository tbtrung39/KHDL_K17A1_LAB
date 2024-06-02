def chep_file(file_nguon, file_ket_qua):
    try:
        with open(file_nguon, 'r', encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print("ko thấy tệp")
        return

    with open(file_ket_qua, 'w', encoding='utf-8') as file:
        file.write(contents)

    print("Nội dung đã đc sao chép")

# Nhập tên tệp từ người dùng
file_nguon = input("Nhập tên tệp tin nguồn: ")
file_ket_qua = input("Nhập tên tệp tin đích: ")

# Thực hiện sao chép nội dung tệp tin
chep_file(file_nguon, file_ket_qua)