file_path = 'BAI6/TABLE.txt'

# Đọc toàn bộ nội dung của file
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 1. Hiển thị nội dung dòng đầu tiên và dòng thứ ba
    if len(lines) >= 1:
        print("Dòng đầu tiên:", lines[0].strip())
    if len(lines) >= 3:
        print("Dòng thứ ba:", lines[2].strip())

    # 2. Hiển thị nội dung toàn bộ file
    print("\nNội dung toàn bộ file:")
    for line in lines:
        print(line.strip())

    # 3. Tìm các số lẻ và ghi vào file ODD.txt
    odd_sos = []
    for line in lines:
        numbers = map(int, line.split())
        odd_sos.extend([num for num in numbers if num % 2 != 0])

    with open('BAI6/ODD.txt', 'w', encoding='utf-8') as odd_file:
        for num in odd_sos:
            odd_file.write(f'{num} ')
    print("\nCác số lẻ đã được ghi vào file ODD.txt")

    # 4. In ra nội dung dòng cuối của file
    if lines:
        print("\nDòng cuối của file:", lines[-1].strip())

except FileNotFoundError:
    print(f"file {file_path} không tồn tại .")
except Exception as e:
    print(f"xuất hiện lỗi: {e}")