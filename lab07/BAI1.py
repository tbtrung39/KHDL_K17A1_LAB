char_set = set()
while True:
    char = input('Nhap vao mot ky tu(an ESC de ket thuc): ')
    if char == 'ESC':
        break
    if not char.isdigit():
        char_set.add(char)
print('Tap hop sau khi loai bo cac ky tu so:',char_set)