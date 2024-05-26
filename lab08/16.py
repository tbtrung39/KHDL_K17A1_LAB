def tao_so_chan():
   n = list(filter(lambda x: x % 2 == 0, range(1, 101)))
   for i in range(0, len(en), 10):
        print(n[i:i+10])
        return n
list_n =tao_so_chan()
print(list_n)