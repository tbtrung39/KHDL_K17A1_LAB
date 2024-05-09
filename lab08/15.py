def create_list(n):
    lst = []
    for i in range(0,n):
        num = int(input(f"Enter the number of element {i+1}:"))
        lst.append(num)
    return lst
def tinh_binh_phuong(lst):
    return list(map(lambda x:x**2,filter(lambda x:x%2!=0,lst)))
n = int(input("Enter the elemts:"))
lst = create_list(n)
square = tinh_binh_phuong(lst)
print(square)