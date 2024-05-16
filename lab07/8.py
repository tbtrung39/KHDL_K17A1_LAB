# viết chương trình sinh tập hợp a bao gồm cả các số nguyên số thực và chuỗi ký tự hãy đếm số phần tử là số nguyên số thực và chuỗi ký tự của tập hợp a
import random
a = []
for _ in range(10):  
    rand_type = random.choice(['int', 'float', 'str'])  
    if rand_type == 'int':
        a.append(random.randint(1, 100)) 
    elif rand_type == 'float':
        a.append(random.uniform(1.0, 100.0)) 
    else:
        a.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))) 
print("Tập hợp a:", a)
int_count = sum(isinstance(x, int) for x in a)
float_count = sum(isinstance(x, float) for x in a)
str_count = sum(isinstance(x, str) for x in a)
print("Số lượng số nguyên trong tập hợp a:", int_count)
print("Số lượng số thực trong tập hợp a:", float_count)
print("Số lượng chuỗi ký tự trong tập hợp a:", str_count)