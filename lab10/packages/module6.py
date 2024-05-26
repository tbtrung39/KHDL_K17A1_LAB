def test(s):
    ki_tu = '0123456789ABCDEF'
    return ''.join([char for char in s if char in ki_tu])

def kiem_tra(s):    

    def nhi_phan(s):
        for char in s:
            if char not in '01':
                return False
        return True

    def he_8(s):
        for char in s:
            if char not in '01234567':
                return False
        return True

    def he_16(s):
        for char in s:
            if char not in '0123456789ABCDEF':
                return False
        return True

    if nhi_phan(s):
        return 2
    elif he_8(s):
        return 8
    elif he_16(s):
        return 16
    else:
        return None


def mot(s):
    return int(s, 2)
def hai(s):
    return int(s, 8)
def ba(s):
    return int(s, 16)