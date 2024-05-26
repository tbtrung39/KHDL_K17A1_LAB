from pk_b1 import is_Tamgiac, Chuvitamgiac, S_Tamgiac 
def main():
    a = float(input("Nhap do dai canh a: "))
    b = float(input("Nhap do dai canh b: "))
    c = float(input("Nhap do dai canh c: "))
    if is_Tamgiac(a, b, c):
        print("Ba so da nhap tao thanh mot tam giac.")
        print("Chu vi tam giac la:", Chuvitamgiac)
        print("Dien tich tam giac la:", S_Tamgiac)
    else:
        print("Ba so da nhap khong tao thanh mot tam giac.") 
        
if __name__ == "__main__":
    main()