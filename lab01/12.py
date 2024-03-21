import math
van_toc_a = int(input('nhập vận tốc của a:'))
# tính từ lúc xe dừng lại thì vt = 0 vậy ta có được 
t = ((van_toc_a)**4)/(math.log(4,5))
print("vậy thời gian tính vận tốc của là:",round(t,2))