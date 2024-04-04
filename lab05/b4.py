str1 = input("nhap chuoi ki tu 1: ")
str2 = input("nhap chuoi ki tu 2: ")
i=0
j=0
S=""
while i < len(str1) and j<len(str2):
    S+=str1[i] + str2[j]
    i+=1
    j+=1
if len(str1) > len(str2):
    S+=str1[i+1::]
else:
    S+=str2[j+1::]
print(S) 