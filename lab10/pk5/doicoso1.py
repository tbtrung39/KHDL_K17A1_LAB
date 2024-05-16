def nhap_so_nguyen():
    """Nhập vào một số nguyên và in ra kết quả vừa nhập."""
    number = int(input("Nhập một số nguyên: "))
    print("Số bạn vừa nhập là:", number)
    return number

def chuyen_sang_nhi_phan(number):
    """Chuyển đổi số đã nhập sang hệ nhị phân và in kết quả ra màn hình."""
    binary = bin(number)
    print("Hệ nhị phân của số", number, "là:", binary)
    return binary

def chuyen_sang_co_so_8(number):
    """Chuyển đổi số đã nhập sang hệ cơ số 8 và in kết quả ra màn hình."""
    octal = oct(number)
    print("Hệ cơ số 8 (bát phân) của số", number, "là:", octal)
    return octal

def chuyen_sang_co_so_16(number):
    """Chuyển đổi số đã nhập sang hệ cơ số 16 và in kết quả ra màn hình."""
    hexadecimal = hex(number)
    print("Hệ cơ số 16 (thập lục phân) của số", number, "là:", hexadecimal)
    return hexadecimal
