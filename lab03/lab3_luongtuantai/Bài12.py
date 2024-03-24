a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def tri_so(n):
 for i in enumerate(a):
    if i[1]==n:
        if i[0]%11==0:
            return i[0]+1
        else:
            return i[0]

print(tri_so("Z"))