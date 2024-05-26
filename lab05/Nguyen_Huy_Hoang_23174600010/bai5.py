Str =  'hellolaptrinh6789'

Str_new=''
for i in Str:
    if i.isdigit():
        Str_new +=i
print('chuỗi sau khi chỉ còn số là ',Str_new)
if Str_new==Str:
    print(Str,'là chuỗi hoàn hảo ')
else:
    print('chuỗi này kp là chuỗi hoàn hảo')