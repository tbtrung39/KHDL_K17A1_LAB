vct_a=map(float, input("Nhập vector a, cách nhau bằng dấu cách: ").split())
vcr_b=map(float, input("Nhập vector b, cách nhau bằng dấu cách: ").split())

ket_qua=sum(map(lambda x,y: x*y, vct_a,vcr_b))

print(ket_qua)