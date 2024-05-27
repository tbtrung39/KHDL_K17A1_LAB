def in_ra(n):
    return n

def cs01(n):
    if n == 0:
        return '0'
    np = ''
    while n > 0:
        np = str(n % 2) + np
        n //= 2
    return np

def cs8p(n):
    if n == 0:
        return '0'
    bp = ''
    while n > 0:
        bp = str(n % 8) + bp
        n //= 8
    return bp

def cs16p(n):
    if n == 0:
        return '0'
    tlp = ''
    hex_chars = "0123456789ABCDEF"    
    while n > 0:
        re = n % 16
        tlp = hex_chars[re] + tlp
        n //= 16  
    return tlp