import random
A = set()
for _ in range(10):
    element_type = random.choice(['int', 'float', 'str'])
    if element_type == 'int':
        A.add(random.randint(1, 100))  
    elif element_type == 'float':
        A.add(random.uniform(1.0, 100.0))  
    else:
       A.add("".join(random.choice("abcdefghijklmnopqrstuvwxyz")))
dem_int = 0
dem_float = 0
dem_str = 0
for element in A:
  if isinstance(element, int):
    dem_int += 1
  elif isinstance(element, float):
    dem_float += 1
  else:
    dem_str += 1
print("Số phần tử là số nguyên:", dem_int)
print("Số phần tử là số thực:", dem_float)
print("Số phần tử là chuỗi ký tự:", dem_str)