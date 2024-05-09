def perform(a,b):
    total = a+b
    minus = a-b
    devide = a//b
    return total,minus,devide
a = int(input("Enter a:"))
b = int(input("Enter b:"))
total,minus,devide = perform(a,b)
print("total:",total)
print("minus:",minus)
print("devide:",devide)