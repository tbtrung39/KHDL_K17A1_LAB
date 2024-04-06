chuoi = input("Nhap mot chuoi ky tu : ")
sum = 0 
for i in chuoi : 
    if not i.isalnum(): 
        sum += 1
print(sum)
