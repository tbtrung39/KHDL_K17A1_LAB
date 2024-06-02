with open("lab11/PASSENGER.IN", mode="r", encoding="utf-8") as file_pass:
    list_chain = file_pass.readlines()

list_number = []
for i in list_chain[1:]:
    list_number.append(list(map(eval, i.split())))

list_number_total = []
for j in list_number:
    list_number_total.append(sum(j))

list_stt_total = []
inx = 0
while inx < len(list_number_total):
    if list_number_total[inx] > 23:
        list_stt_total.append(inx + 1)
    inx += 1

list_number_total_chain = []
for number in list_number_total:
    list_number_total_chain.append(str(number) + "\n")

list_quantity = []
for k in list_number:
    list_quantity.append(len(k))
print(list_quantity)

list_stt_quantity = []
for l in list_quantity:
    if l > 5:
        list_stt_quantity.append(l)

list_stt = set(list_stt_quantity) and set(list_stt_total)

list_stt_false = []
for chr in list_stt:
    list_stt_false.append(str(chr) + "\n")

with open("lab11/WEIGHT.OUT", mode="w") as file_weight:
    file_weight.writelines(list_number_total_chain)

with open("lab11/CANCELED.OUT", mode="w") as file_canceled:
    file_canceled.writelines(list_stt_false)