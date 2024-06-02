def copy_file_contents(source_file, dest_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("Nguồn tin nhắn không tồn tại. Kết thúc chương trình.")
        return

    with open(dest_file, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Tệp tin nội dung {source_file} đã được sao chép sang {dest_file}.")

# Nhập tên tệp từ người dùng
source_file = input("Nhập tên tệp tin nguồn: ")
dest_file = input("Nhập tên tệp đích: ")

# Thực hiện sao chép nội dung tệp tin
copy_file_contents(source_file, dest_file)
