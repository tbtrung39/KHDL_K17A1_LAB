a = input("Nhập số n: ")
b = False
while not b:
    if a.isdigit() and int(a) > 0:
        n = int(a)
        b = True
    else:
        print("Vui lòng nhập một số nguyên dương.")
        a = input("Nhập số n: ")
c= [0, 1]
if n > 2:
    for i in range(2, n):
        next_fib = c[-1] + c[-2]
        c.append(next_fib)
y = ""
for num in c:
    y += str(num) + ","
    
y  = y.rstrip(", ")  

print("Dãy bđến số bthứ", n, "là:")
print(y)