# Read the input file
with open("lab11/PASSENGER.IN", mode="r", encoding="utf-8") as file_pass:
    list_chain = file_pass.readlines()

list_number = []
for i in list_chain[1:]:
    list_number.append(list(map(eval, i.split())))

list_number_total = []
for j in list_number:
    list_number_total.append(sum(j))

list_stt_total = []
index = 0
while index < len(list_number_total):
    if list_number_total[index] > 23:
        list_stt_total.append(index + 1)
    index += 1

list_number_total_chain = []
for num in list_number_total:
    list_number_total_chain.append(str(num) + "\n")

list_quantity = []
for k in list_number:
    list_quantity.append(len(k))
print(list_quantity)

list_stt_quantity = []
for l in range(len(list_quantity)):
    if list_quantity[l] > 5:
        list_stt_quantity.append(l + 1)

list_stt = set(list_stt_quantity).intersection(set(list_stt_total))

list_stt_false = []
for chr in list_stt:
    list_stt_false.append(str(chr) + "\n")

with open("lab11/WEIGHT.OUT", mode="w") as file_weight:
    file_weight.writelines(list_number_total_chain)

with open("lab11/CANCELED.OUT", mode="w") as file_canceled:
    file_canceled.writelines(list_stt_false)
