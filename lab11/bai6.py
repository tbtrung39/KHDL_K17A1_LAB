print('ket qua cau a:')
#a
with open(file='lab11\ma_tran_so.txt', mode='r',encoding='utf-8') as file:
    print(file.readline().strip())
    file.readline()
    print(file.readline().strip())

print("ket qua cau b")
#b
with open(file='lab11\ma_tran_so.txt', mode='r',encoding='utf-8') as file:
    lines=file.readlines()
    for line in lines:
        print(line.strip())

#c
def kt_so_le(so):
    return so&2!=0

def doc_file(path):
    with open (path,'r',encoding='utf-8') as file:
        lines =file.read()
    cac_so=[int(so) for so in lines.split()]
    return cac_so

def ghi_so(cac_so, path):
    so_le=[so for so in cac_so if kt_so_le(so)]
    ma_tran=[]
    for i in range(4):
        hang=[]
        for j in range(4):
            if so_le:
                hang.append(str(so_le.pop(0)))
            else:
                hang.append('0')
        ma_tran.append(hang)
    
    with open (path,'w',encoding='utf-8') as file:
        for hang in ma_tran:
            file.write(''.join(hang)+'\n')

duong_dan_1='lab11\ma_tran_so.txt'
duong_dan_2='lab11\ODD.txt'
cac_so=doc_file(duong_dan_1)
ghi_so(cac_so, duong_dan_2)

print('ket qua cau d:')
#d
with open(file='lab11\ODD.txt', mode='r',encoding='utf-8') as file:
    file.readline()
    file.readline()
    file.readline()
    print(file.readline().strip())