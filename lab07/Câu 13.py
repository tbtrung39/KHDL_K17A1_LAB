'''
. Nhập vào chuỗi ký tự, hãy tạo ra một từ điền (dictionary) có các thành phần con là các
Cap (K, V) trong d6 K la mot chuoi con lien tiep nao do cia W va V la so lan xuat hien
của K trong W.
'''
chuoi = input("Nhập vào chuỗi ký tự: ")
dict_chuoi_con = {}
do_dai = len(chuoi)
for i in range(do_dai):
    for j in range(i + 1, do_dai + 1):
        chuoi_con = chuoi[i:j]
        dict_chuoi_con[chuoi_con] = None
print("Các chuỗi con trong từ điển:")
for key in dict_chuoi_con:
    print(key)