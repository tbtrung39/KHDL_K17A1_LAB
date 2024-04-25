n = int(input("Enter the numbers: "))
set_a = {}
for i in range(1,n+1):
    set_a[i]=i*i
print(f"Dictionary chứa các cặp (i, i*i) từ 1 đến {n} là: {set_a}")