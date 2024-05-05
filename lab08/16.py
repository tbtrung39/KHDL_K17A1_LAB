def list_chan():
    chan = [ i for i in range(1,1001) if i % 2 == 0]
    return chan

chan = list_chan()
print("list các số chẵn là:",chan)