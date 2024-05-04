def enter_infor():
    hoten = input("Enter name:")
    quequan = input("Enter country:")
    tham_nien = int(input("Enter length of service:"))
    return hoten,quequan,tham_nien
def wage_cost(tham_nien):
    basic_salary = 5000000
    percent_salary=1+(basic_salary*0.01)
    return basic_salary*percent_salary
def output_infor(hoten,quequan,tham_nien,luong):
    print(f"hoten {hoten}")
    print(f"quequan:{quequan}")
    print(f"thamnien: {tham_nien}")
    print(f"Luong:{luong}")
def main():
    hoten,quequan,tham_nien=enter_infor()
    luong=wage_cost(tham_nien)
    output_infor(hoten,quequan,tham_nien,luong)
main()