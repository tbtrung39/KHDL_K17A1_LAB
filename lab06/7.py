list=[['mon',73],['tue',89],['wed',95],['thu',103],['fri',115],['sat',128],['sum',120]]
for i in list:
    print(i)
print(list[2][1])
#
print(len(list))
list.append(['random',150])
print(len(list))
#
total_sale=0
for i in list:
    if i[0]in['tue','wed','sat','sun']:
        total_sale+=i[1]
print(total_sale)