from packages import input_item_info,print_item_info,calculate_total_price
item_code, unit_price, quantity = input_item_info()
total_price = calculate_total_price(unit_price, quantity)
print_item_info(item_code, unit_price, quantity, total_price)