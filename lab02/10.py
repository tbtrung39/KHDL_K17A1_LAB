start_time = int(input("Nhập giờ bắt đầu (5-22): "))
end_time = int(input("Nhập giờ kết thúc (5-22): "))
time = end_time - start_time

if time <= 0 or start_time < 5 or end_time > 22:
    print("Nhập sai giờ hoặc giờ không hợp lệ.")
else:
    price = 0
    if time > 3:
        price += 3 * 100000
        time -= 3
        hour_price = 100000 * 0.75
        price += time * hour_price
    else:
        price = time * 100000

    if 11 <= start_time and end_time <= 15:
        price *= 0.9  # 10% giảm giá
    print(f"Tiền phải trả: {price}")