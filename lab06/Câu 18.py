'''
Ma trận mxn (m hàng, n cột) có thể được mô tả bởi danh sách như sau:
A=[[a11, a12, ...aln], [a21, a22,...,a2n], ...,[(am1, am2, ..., amn)].
Thực hiện các công việc sau:
a. Viết chương trình nhập vào ma trận A với các phần tử aij là các số tự nhiên được nhập từ bàn phím.
b. Tính tổng các phần tử của Ma trận A.
'''
def nhap_ma_tran(m, n):
    ma_tran = []
    for i in range(m):
        hang = []
        for j in range(n):
            hang.append(int(input(f"Nhập phần tử A[{i+1},{j+1}]: ")))
        ma_tran.append(hang)
    return ma_tran

def tinh_tong(ma_tran):
    tong = 0
    for hang in ma_tran:
        tong += sum(hang)
    return tong

def main():
    #Nhập số hàng và số cột của ma trận
    m = int(input("Nhập số hàng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))

    #Nhập ma trận từ bàn phím
    A = nhap_ma_tran(m, n)

    #Tính tổng các phần tử của ma trận
    tong = tinh_tong(A)

    #In ra tổng các phần tử của ma trận
    print("Tổng các phần tử của ma trận là:", tong)

if __name__ == "__main__":
    main()
