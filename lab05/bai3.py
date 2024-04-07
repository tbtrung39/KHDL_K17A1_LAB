n= int(input("nhập số tự nhiên : "))
sonhiphan=[]
while n>0:
    sonhiphan.append(str(n%2))
    n//=2
sonhiphan=''.join(sonhiphan[::-1])
print(sonhiphan)

