str1=input("nhập chuỗi ký tự 1: ")
str2=input("nhập chuỗi ký tự 2: ")
luutru=[]
dodaistr1=len(str1)
dodaistr2=len(str2)
chisostr1=0
chisostr2=0
while chisostr1 < dodaistr1 and chisostr2<dodaistr2:
    luutru +=str1[chisostr1]+str2[chisostr2]
    chisostr1+=1
    chisostr2+=1
luutru+=str1[chisostr1:]+str2[chisostr2:]
print(luutru)