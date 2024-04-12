'''
Viết chương trình sinh một dãy list A gồm 1000 số tự nhiên, nằm ngẫu nhiên trong khoảng [1,99999]. 
Sau đó sắp xếp lại theo thứ tự tăng dần theo 2 cách. Sử dụng hàm sorted() và không sử dụng hàm sorted().
'''
import random
A = []
for a in range(1000):
    number = random.randint(0,100000)
    A.append(number)

#Sử dụng hàm sorted()
A_sorted = sorted(A)
print("Sắp xếp list A sử dụng hàm sorted():")
print(A_sorted)

#Không sử dụng hàm sorted()
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[j] < A[i]:
            i = j
    A[i], A[i] = A[i], A[i]
print("Danh sách A gồm 1000 số tự nhiên sau khi được sắp xếp:")
print(A)
