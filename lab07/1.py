khoi_tao_set= set()

while True:
    char = input("Nhập ký tự (hoặc nhấn 'EXC' để kết thúc): ")
    if char == 'EXC':
        break
    khoi_tao_set.add(''.join(filter(lambda x: not x.isdigit(), char)))

print("Tập hợp sau khi loại bỏ ký tự số:", khoi_tao_set)