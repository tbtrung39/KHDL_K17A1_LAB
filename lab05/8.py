str = input("Nhập chuỗi ký tự: ")
max_length = 0
max_substring = ""
for i in range(len(str)):
    for j in range(i+1, len(str)+1):
        substring = str[i:j]
        if all(char == substring[0] for char in substring):
            if len(substring) > max_length:
                max_length = len(substring)
                max_substring = substring
print(f"''{max_substring}''")