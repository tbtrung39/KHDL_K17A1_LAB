def min_max(a,b,c):
    lst = [a,b,c]
    maxstr = max(lst)
    minstr = min(lst)
    return maxstr,minstr
a = int(input("nhập vào số nguyên a: "))
b = int(input("nhập vào số nguyên b: "))
c = int(input("nhập vào số nguyên c: "))
min_max(a,b,c)
print(f"giá trị max và min của dãy số lần lượt là {min_max(a,b,c)}")