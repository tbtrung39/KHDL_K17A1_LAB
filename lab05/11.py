Str1 = "Khoa, khoa hoc ung dung"
words = Str1.split(", ")
words = [word for sublist in [word.split(" ") for word in words] for word in sublist]
for word in words:
    print(word)
