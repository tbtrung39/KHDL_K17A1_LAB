'''
Viết chương trình tìm các số hoàn hảo nhỏ hơn n 
(với n được nhập từ bàn phím).
'''
n = int(input("Nhập vào một số n "))
sum= 0
for i in range (1,n):
    if n%i== 0:
        sum +=i
        print(f"{n} là số hoàn hảo ")
else : 
    print(f"{n} không phải là số hoàn hảo " )