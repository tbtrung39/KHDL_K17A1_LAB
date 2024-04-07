Str = '''Rất muốn yêu nhưng bố mẹ cấm 
Vậy tỏ tình là câu có tội'''
word = Str.split()
find=str(input('Nhap tu can tim:'))
list=[]
for i in word:
    if i ==find:
        list.append(i)
print(f'Từ {find} xuất hiện trong đoạn thơ trên {len(list)} lần.')