str1=input('Nhap ki tu chuoi:')
str2=input('Nhap ki tu chuoi:')
xao_tron=''
do_dai_2_chuoi=min(len(str1),len(str2))
for i in range(do_dai_2_chuoi):
    xao_tron+=str1[i]+str2[i]
xao_tron+=str1[do_dai_2_chuoi:]+str2[do_dai_2_chuoi:]
print('Chuoi tron:',xao_tron)
if len(str1)>len(str2):
    xao_tron+=str1[do_dai_2_chuoi:]
elif len(str2)>len(str1):
    xao_tron+=str2[do_dai_2_chuoi:]
    print('Chuoi tron:',xao_tron)