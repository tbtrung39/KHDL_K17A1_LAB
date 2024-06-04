def copyFile(source,dest):
    try:
        with open(source,'r',encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print('Tâp tin này không tồn tại.')
        return
    with open(dest,'w',encoding='utf-8') as file:
        file.write(content)
    print(f'Nội dung từ tập tin {source} đã được sao chép sang {dest}.')

#Nhập dl
source=input('Nhập đường dẫn nguồn:')
dest=input('Nhập đường dẫn đích:')

#Sao chép nd
copyFile(source,dest)