'''
Viết chương trình nhập 2 số tự nhiên m, n. Tính tổng các chữ số chung của m và n. 
Ví dụ m=1123499, n=112229; có chữ số chung là 1,2,9 do đó tổng các chữ số chung bằng 1+2+9=12.
Trường hợp có một chữ số xuất hiện nhiều lần trong cả m và n thì chữ số đó chỉ được tính một lần.
'''
m=set(str(int(input("Nhap vao gia trị m:"))))
n=set(str(int(input("Nhap vao gia trị n:"))))
q=m.intersection(n) 
result =0
for i in q:
    result = result + int(i)

print(result)