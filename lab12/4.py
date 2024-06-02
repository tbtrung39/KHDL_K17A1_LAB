def read_and_write_file():
    try:
        input_file_name = input("Nhập tên tập tin cần đọc: ")
        output_file_name = input("Nhập tên tập tin cần ghi: ")

        # Đọc tập tin
        with open(input_file_name, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Ghi tập tin
        with open(output_file_name, 'w', encoding='utf-8') as outfile:
            outfile.write(content)

        print(f"Đã ghi nội dung vào tập tin {output_file_name}.")
    except FileNotFoundError:
        print("Không tìm thấy tập tin với tên vừa nhập.")
    except IOError:
        print("Lỗi xảy ra khi mở hoặc ghi tập tin.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
    finally:
        try:
            infile.close()
            outfile.close()
        except NameError:
            pass  # If infile or outfile was not defined due to an error, pass

read_and_write_file()