import pack1.modul1 as t

a = 3
b = 4
c = 5

if t.isTamGiac(a, b, c):
    print("Đây là một tam giác.")
    cv = t.ChuViTamGiac(a, b, c)
    s =  t.S_TamGiac(a, b, c)
    print('chu vi tam giác là:', cv)
    print('diện tích tam giác là:', s)
else:
    print("Đây không phải là một tam giác.")