def remove_invalid_chars(input_str):
    """
    Loại bỏ tất cả các ký tự không thuộc vào tập hợp {0,1,2,...,9,A,B,C,D,E,F} trong chuỗi đầu vào.
    """
    valid_chars = '0123456789ABCDEF'
    invalid_chars = [char for char in input_str if char.upper() not in valid_chars]
    clean_str = ''.join(char for char in input_str if char.upper() in valid_chars)
    return clean_str, invalid_chars

def get_base(input_str):
    """
    Xác định cơ số của một chuỗi số.
    """
    if all(char in '01' for char in input_str):
        return 2
    elif all(char in '01234567' for char in input_str):
        return 8
    elif all(char in '0123456789ABCDEF' for char in input_str):
        return 16
    else:
        return None

def convert_to_base10(input_str, base):
    """
    Chuyển đổi một chuỗi số từ cơ số `base` sang cơ số 10.
    """
    valid_chars = '0123456789ABCDEF'
    value = 0
    for char in input_str:
        value = value * base + valid_chars.index(char.upper())
    return value