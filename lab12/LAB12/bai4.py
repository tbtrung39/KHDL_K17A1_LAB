def copy_file_contents(source_file, dest_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print("Tệp tin nguồn không tồn tại. Chương trình kết thúc.")
        return

    with open(dest_file, 'w', encoding='utf-8') as file:
        file.write(contents)

    print(f"Nội dung tệp tin {source_file} đã được sao chép sang {dest_file}.")

# Nhập tên tệp từ người dùng
source_file = input("Nhập tên tệp tin nguồn: ")
dest_file = input("Nhập tên tệp tin đích: ")

# Thực hiện sao chép nội dung tệp tin
copy_file_contents(source_file, dest_file)