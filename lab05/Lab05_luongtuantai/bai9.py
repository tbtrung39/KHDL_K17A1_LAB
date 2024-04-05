input_str = input("Nhập chuỗi ký tự: ")
str_cuc_dai = ""
str_gan_nhat = ""
for i in range(len(input_str)):
    if i > 0 and input_str[i] == input_str[i - 1]:
        str_gan_nhat += input_str[i]
    else:
        str_gan_nhat = input_str[i]
    if len(str_gan_nhat) > len(str_cuc_dai):
        str_cuc_dai = str_gan_nhat
print("Chuỗi con có độ dài cực đại và bao gồm các ký tự giống nhau:", str_cuc_dai)
