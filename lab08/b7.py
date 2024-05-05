def max_min(x,y,z):
    max = x
    if max < y:
        max = y
    elif max < z:
        max =z
    min = x 
    if min >y:
        min =y
    elif min > z:
        min = z
    print("so lon nhat la:",max)
    print("so nho nhat la:",min)
    return

x = int(input("nhap x: "))
y = int(input("nhap y: "))
z = int(input("nhap z: "))
max_min(x,y,z)