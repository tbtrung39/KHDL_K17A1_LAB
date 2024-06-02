def nt(x):
    list = []
    for i in range(2,x+1):
        nt = True
        for j  in range(2,i):
            if i%j==0:
                nt = False
                break
        if nt:
          list.append(i)
    return list
a=  int(input('nhập số để kiểm tra: '))
print('số nguyên tố từ nhỏ hơn',a,'là:',nt(a))