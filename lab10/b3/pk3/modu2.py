def uoc(n):
    t =0
    for i in range(1, n + 1):
        if n % i == 0:
            t+=i
    return t
