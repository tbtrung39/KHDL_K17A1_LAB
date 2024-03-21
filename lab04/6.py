# Dictionary chứa mapping giữa số và chữ cái tương ứng
number_words = {
    '0': 'không',
    '1': 'một',
    '2': 'hai',
    '3': 'ba',
    '4': 'bốn',
    '5': 'năm',
    '6': 'sáu',
    '7': 'bảy',
    '8': 'tám',
    '9': 'chín'
}

# Nhập số từ bàn phím
number = input("Nhập một số từ bàn phím: ")

# Chuyển đổi số thành chữ
word = ''
i = 0
while i < len(number):
    digit = number[i]
    if digit in number_words:
        word += number_words[digit] + ' '
    i += 1

# In ra số dưới dạng chữ
print(f"Số {number} được viết dưới dạng chữ là: {word}")
