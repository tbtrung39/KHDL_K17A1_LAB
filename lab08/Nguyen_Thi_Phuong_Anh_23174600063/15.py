n = int(input("Sô nguyên:"))

def list_int(n):
    list = []
    for i in range(n):
        i = int(input(f"Số nguyên thứ {i+1}:"))
        list.append(i)
    return list

listbp = list_int(n)

bp = list ( map ( lambda i : i**2 , filter( lambda i : i % 2 != 0 , listbp )))
print(f"list final lẻ: {bp}")
       