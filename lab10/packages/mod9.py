def input_item_info():
    item_code = input("Nhập mã hàng: ")
    unit_price = float(input("Nhập đơn giá: "))
    quantity = int(input("Nhập số lượng: ")) 
    return item_code, unit_price, quantity
def calculate_total_price(unit_price, quantity):
    return unit_price * quantity
def print_item_info(item_code, unit_price, quantity, total_price):
    print(f"Mã hàng: {item_code}")
    print(f"Đơn giá: {unit_price}")
    print(f"Số lượng: {quantity}")
    print(f"Thành tiền: {total_price}")