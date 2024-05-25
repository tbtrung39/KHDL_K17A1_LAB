def doc_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read()
    cac_so = {int(so) for so in lines.split()}
    return cac_so

def ghi_so(cac_so, path):
    with open(path, 'w', encoding='utf-8') as file:
        for so in sorted(cac_so):
            file.write(f'{so}\n')

duong_dan_m = r'lab11\m_num.txt'
duong_dan_n = r'lab11\n_num.txt'
duong_dan_so_chung = r'lab11\so_chung.txt'

so_cua_m = doc_file(duong_dan_m)
so_cua_n = doc_file(duong_dan_n)

cac_so_chung_cua_m_va_n = so_cua_m & so_cua_n

ghi_so(cac_so_chung_cua_m_va_n, duong_dan_so_chung)


with open(duong_dan_so_chung, 'r', encoding='utf-8') as file:
    noi_dung = file.read()
print(noi_dung)
