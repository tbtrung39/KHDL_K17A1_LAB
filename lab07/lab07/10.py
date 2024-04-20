m = int(input("Nhập số tự nhiên thứ nhất (m): "))
n = int(input("Nhập số tự nhiên thứ hai (n): "))
m_str = str(m)
n_str = str(n)
chu_so_chung = set()
for digit in m_str:
    if digit in n_str and digit not in chu_so_chung:
        chu_so_chung.add(int(digit))
sum_common = sum(chu_so_chung)
# In ra tổng các chữ số chung của m và n
print("Tổng các chữ số chung của m và n:", sum_common)
