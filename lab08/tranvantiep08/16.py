def tao_ds() :
    lisst = []
    for i in range(1, 101): 
        if i % 2 == 0 : 
            lisst.append(i)
    return lisst

print(tao_ds())

# cách khác 
list_moi = list(filter(lambda x: x % 2 == 0, range(1, 101)))
print(list_moi)