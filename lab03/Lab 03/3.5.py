'''
Viết chương trình vẽ hình chữ nhật và điền dấu * như hình sau:
* * * * *
* * * * *
* * * * *
'''
chieu_dai = 3
chieu_rong = 5

for i in range(chieu_dai):
    for j in range(chieu_rong):
        print("*",end="")
    print()