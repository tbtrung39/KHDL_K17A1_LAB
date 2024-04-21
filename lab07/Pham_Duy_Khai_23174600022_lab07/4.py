a=[161,182,161,154,176,170,167,171,170,174,150,142,148,165,170,178,156,145,149,163,162,159,165,165,170,180,155,159,155,153,152,162,180,168,169,168,167,170]
print(a)
print('nhóm có',len(a),'sinh viên')
print('chiều cao trung bình của các sinh viên:',sum(a)/len(a))
print(f'các chiều cao khác nhau trong nhóm bao gồm:{set(a)}\n chiều cao trung bình của nhóm:{sum(set(a))/len(set(a))}')
