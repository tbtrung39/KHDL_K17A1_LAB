list1 = [10,9,8,7,6,5,4,3,2,1]
list2 =['hoa','lan','nam','mai','dao','binh','dat','khanh','hoai','xuan']
tu_dien = {list1[i] : list2[i] for i in range(len(list1))}
for so,ten in tu_dien.items():
    print(f"{so}:{ten}")