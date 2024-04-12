'''
Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. 
Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
Lưu ý: i=0,1,..
.,X-1; j=0,1,..., Y-1.
Ví dụ:
giá trị X, Y nhập vào là 3, 5 thì đầu ra là:[[0, 0, 0, 0, 01, [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]].
'''
def tao_mang_2_chieu(X, Y):
    mang_2_chieu = []
    for i in range(X):
        hang = []
        for j in range(Y):
            hang.append(i * j)
        mang_2_chieu.append(hang)
    return mang_2_chieu

def main():
    #Nhập giá trị X, Y từ người dùng
    X = int(input("Nhập giá trị X: "))
    Y = int(input("Nhập giá trị Y: "))

    #Tạo và in ra mảng 2 chiều
    mang = tao_mang_2_chieu(X, Y)
    print("Mảng 2 chiều đã tạo:")
    for hang in mang:
        print(hang)

if __name__ == "__main__":
    main()
