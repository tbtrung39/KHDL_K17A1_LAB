filename = input("Nhập tên tệp: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print("Lỗi: Tệp không tồn tại.")
else:
    try:
        with open('Copy.dat', 'w', encoding='utf-8') as copy_file:
            copy_file.write(content)
            print("Nội dung đã được sao chép vào Copy.dat")
    except Exception as e:
        print(f"Lỗi khi ghi tệp: {e}")
