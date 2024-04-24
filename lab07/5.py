# viết chương trình tạo tập hợp a gồm 5 phần tử ngẫu nhiên được lấy  từ một danh sách 10 phần tử là các số 0,1,...9
import random
so = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = set(random.sample(so, 5))
print("Tập hợp a:", a)