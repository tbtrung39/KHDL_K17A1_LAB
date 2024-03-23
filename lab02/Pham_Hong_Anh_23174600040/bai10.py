start=int(input('nhập giờ bắt đầu(5->22):'))
end=int(input('nhập giờ kết thúc(5->22):'))
thoi_gian=end-start 
if thoi_gian<=3:
    tien=thoi_gian*100000
else:
    tien=thoi_gian*100000*(3/4)
if 11<=start<=14 and 12<=end<=15:
    tien=tien*(9/10)
print('tiền phải trả: ',tien)