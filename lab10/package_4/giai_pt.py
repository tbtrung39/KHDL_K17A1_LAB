import math

def giai_pt_bac_nhat_mot_an(a,b):
    if a==0:
        if b==0:
            return "pt vo so nghiem"
        else:
            return "pt vo nghiem"
    else:
        x=-b/a
        return f"nghiem cua cua pt la: x={x}"

def giai_pt_bac_2(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                return 'pt vo so nghiem'
            else:
                return 'pt vo nghiem'
        else:
            return f"pt co nghiem duy nhat x={-c/b}"
    delta=b**2 - 4*a*c
    if delta >0:
        x1=(-b + math.sqrt(delta))/(2*a)
        x2=(-b - math.sqrt(delta))/(2*a)
        return f'pt co 2 nghiem phan biet x1={x1}, x2={x2}'
    if delta ==0:
        x=-b/(2*a)
        return f'pt co nghiem kep: x={x}'
    else:
        return 'pt vo nghiem'