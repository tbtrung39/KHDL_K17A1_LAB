#câu 5
#viết phương trình tạo 1 dãy list A gồm 1000 số tự nhiên, nằm ngẫu nhiên trong khoảng 1-99999
import random
A = [random.randint(1, 99999) for i in range(1000)]
print(A)
