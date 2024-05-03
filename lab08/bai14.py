def tao_list_binh_phuong():
    n = int(input("nhap so phan tu: "))
    list1 = []
    for i in range(n):
        list1.append(int(input("nhap so nguyen: ")))
    print(list1)
    list2 = list(map(lambda x: x**2, list1))
    return list2

list2 = tao_list_binh_phuong()