'''Cho trước (hoặc nhập từ bàn phím) chuỗi ký tự Str, có bao nhiêu ký tự không phải là 
chữ cái tiếng Anh và không là số trong chuỗi Str. '''
chuoi =' my name is jack 5 cu'
dem=0
for i in chuoi:
    if not i=='j' and not i =='f'and not i=='w'and not i=='z' and not '1' <= i <='9':
        dem+=1
print(" so ky tu khong phai la tieng anh va so la",dem)
