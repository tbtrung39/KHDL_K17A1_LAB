def sort_words(input_string):
    words = input_string.split(',')
    words.sort()
    return ','.join(words)

input_string = input("Nhập chuỗi các từ, phân tách bởi dấu phẩy: ")
result = sort_words(input_string)
print(result)