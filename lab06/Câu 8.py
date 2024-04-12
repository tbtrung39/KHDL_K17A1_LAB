'''
Với n được nhập vào từ bàn phím. Hãy viết chương trình sử dụng list comprehension 
để in dãy Fibonacci dưới dạng tách biệt bằng dấu ",",
Ví dụ: Nếu n được nhập là 7 thì chương trình sẽ in ra: 0, 1, 1, 2, 3, 5, 8, 13.
'''
n = int(input("Nhập số lượng số Fibonacci: "))

#Tạo dãy Fibonacci sử dụng list comprehension
fibonacci = [
    0 if i == 0 else 
    1 if i == 1 else 
    fibonacci[i-1] + fibonacci[i-2] 
    for i in range(n)
]

#In dãy Fibonacci dưới dạng tách biệt bằng dấu ","
print("Dãy Fibonacci:", end=" ")
print(*fibonacci, sep=", ")
