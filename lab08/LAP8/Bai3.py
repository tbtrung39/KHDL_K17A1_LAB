def songuyento(a):
    if a<=1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
n=int(input("nhập số nguyên n:"))
def songuyentonhohonn(n):
    list=[]
    for a in range(2,n): #Duyệt qua tất cả các số từ 2 đến n-1
        if songuyento(a):
            list.append(a)
    return list
print("các số nguyên tố nhỏ hơn",n,"là:")
print(songuyentonhohonn(n))