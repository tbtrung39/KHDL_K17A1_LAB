Str = '''Bầy chim mừng rỡ hót vang
Vườn hoa trước ngõ bướm vàng nhởn nhơ
Mẹ em phơi lụa hồng tơ
Ngắm mây em viết bài thơ yêu đời
Nắng hòa mưa thuận khắp nơi
Em mơ em ước mọi người ấm no.'''


words = Str.split()

find=  str(input('nhập từ cần tìm ở đây : '))
list =[]
for i in words:
    if i ==find:
        list.append(i)

print('từ ',find,'xuất hiện trong đoạn thơ trên ',len(list),'lần')