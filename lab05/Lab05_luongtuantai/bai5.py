str=input("Nhập chuỗi ký tự: ")
str_so=''
for i in str:
    if i.isdigit():
        str_so+=i
print("chuỗi số là:", str_so)
so=int(str_so)
tong_uoc=0
for j in range(1,so):
    if so==0:
        tong_uoc+=j
if tong_uoc==so:
    print(so, "là số hoàn hảo")
else:
    print(so, 'không phải là số hoàn hảo')