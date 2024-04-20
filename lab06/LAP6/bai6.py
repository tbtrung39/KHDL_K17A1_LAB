random= [(i*4673+4747747)% 99 +1 for i in range(10)]
print(random)
print('Sắp xếp theo thứ tự tăng dần:',sorted(random))

#không dùng sorted
random.sort()
print('Thứ tự tăng dần:',random)


