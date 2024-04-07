Str1=input('nhap chuoi 1:')
Str2=input('nhap chuoi 2:')
len1=len(Str1)
len2=len(Str2)
t_str=''
i=0
j=0
while i<len1 or j < len2:
    if i<len1:
        t_str+= Str1[i]
        i+=1
    if j<len2:
        t_str+= Str2[j]
        j+=1
print('chuoi so sau khi lam tron:',t_str)