def uoc_so_nguyen_to(n):
    i = 2
    uoc_so = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            uoc_so.add(i)
    if n > 1:
        uoc_so.add(n)
    return uoc_so

with open('lab11/bai4/f_in.dat', 'r') as f_in, open('lab11/bai4/f_out.dat', 'w') as f_out:
    for dong in f_in:
        so = int(dong.strip())
        uoc_so = uoc_so_nguyen_to(so)
        f_out.write(' '.join(map(str, uoc_so)) + '\n')
