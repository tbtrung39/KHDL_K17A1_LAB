def uoc_so(n):
    uoc = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc.append(i)
    return uoc

n = int(input("n: "))
cac_uoc_so = uoc_so(n)
print("ước số", cac_uoc_so)