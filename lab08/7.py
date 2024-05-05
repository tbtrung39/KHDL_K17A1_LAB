# viết chương trình nhập 3 số nguyên a ,b , c 
def max_min(a,b,c):
    return a,b,c
gia_tri_a = int(input("nhập vào giá trị của a:"))
gia_tri_b  = int(input("nhập vào giá trị của b:"))
gia_tri_c = int(input("nhập vào giá trị của c:"))
gia_tri = max_min(gia_tri_a,gia_tri_b,gia_tri_c)
print("giá trị của a b c là", gia_tri)
print("giá trị lớn nhất ", max(gia_tri))
print("giá trị nhỏ nhất:",min(gia_tri))
    