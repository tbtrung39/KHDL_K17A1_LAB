# viết chương trình nhập một số thập phân và sau đó chuyển đổi thành dạng kí tự ví dụ 324 
a = {0:"không",
     1:"một",
     2:"hai",
     3:"ba",
     4:"bốn",
     5:"năm",
     6:"sáu",
     7:"bảy",
     8:"tám",
     9:"chín"}

n = int(input("nhập một số thập phân từ bàn phím:"))
name = ''
i = 0
while True:
    if i < len(n):
        b = n[i]
        for b in a:
            name += a[b] + ''
        i += 1
    print(f"số{n} và in ra các chữ só đọc được là {name}") 


