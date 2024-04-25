def ps_circle(r):
    pi = 3.14
    s = pi * (r**2)
    P = 2 * pi * r
    return s,P
r = int(input("nhập vào bán kính của hình tròn: "))
ps_circle(r)
print(f"diện tích và chu vi của hình tròn bán kính {r} = {ps_circle(r)}")