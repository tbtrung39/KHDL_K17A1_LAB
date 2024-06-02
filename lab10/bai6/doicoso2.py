def filter_hex_chars(input_str):
    """Loại bỏ các ký tự không thuộc tập hợp {0,1,2,3,...,9,A,B,C,D,E,F}."""
    valid_chars = set('0123456789ABCDEF')
    result = ''.join([char for char in input_str if char in valid_chars])
    print(f"Chuỗi kết quả: {result}")
    return result

def detect_base(input_str):
    """Cho biết một chuỗi số cho trước là biểu diễn cơ số mấy."""
    if all(char in '01' for char in input_str):
        return 2
    elif all(char in '01234567' for char in input_str):
        return 8
    elif all(char in '0123456789' for char in input_str):
        return 10
    elif all(char in '0123456789ABCDEF' for char in input_str.upper()):
        return 16
    else:
        return "Không xác định"

def convert_base_to_decimal(input_str, base):
    """Chuyển đổi một chuỗi số từ cơ số bất kỳ sang cơ số 10."""
    try:
        decimal_value = int(input_str, base)
        print(f"Số {input_str} ở cơ số {base} sang cơ số 10 là: {decimal_value}")
        return decimal_value
    except ValueError:
        print("Chuỗi không hợp lệ cho cơ số này.")
        return None