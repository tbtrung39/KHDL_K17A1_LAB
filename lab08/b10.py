def uoc(n):
    lst = []
    for i in range(1,n):
        if n % i==0:
            lst.append(i)
    return lst

x= int(input("nhap vao mot so nguyen: "))
print("uoc cua",x,"la: ",uoc(x))

