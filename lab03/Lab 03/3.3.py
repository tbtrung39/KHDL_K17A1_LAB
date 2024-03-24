'''
Viết chương trình xét xem một số n có phải là số nguyên tố không. 
Nếu không phải hãy in ra số nguyên tố gần n nhất?
'''
n = int(input("Nhập vào số n: "))
for i in range (n,0,-1):
    # i sẽ là các số nhỏ hơn n
    # kiểm tra i xem có phải số nguyên tố không 
    for j in range (0,i):
        if j == 0 or j == 1 :
            continue
        if i%j == 0 :
            break
    else : 
        print(i, "  là số nguyên tó ")
        break
