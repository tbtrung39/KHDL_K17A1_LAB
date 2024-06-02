file_path='6\ODD.txt'
def f4(file_path):
    with open(file_path, 'r') as file:
        lines=file.readlines()
        if lines:
            print('Dòng cuối cùng:',lines[-1].strip())
        else:
            print('Tập tin rỗng.')
f4(file_path)

