def so_ngto(a):
    if a<=1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
n=int(input("nhập số nguyên n:"))
def so_ngto_nho_hon(n):
    list=[]
    for a in range(2,n): #Duyệt qua tất cả các số từ 2 đến n-1
        if so_ngto(a):
            list.append(a)
    return list
print("các số nguyên tố nhỏ hơn",n,"là:")
print(so_ngto_nho_hon(n))