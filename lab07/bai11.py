c={1,2,3,4,5,6,7,8,9,10,11}
j={1,3,6,7,8}
p={1,4,3,9,10,11}
tap_hop_3_code= c & j & p
print(tap_hop_3_code)

tap_hop_2_code=(c.intersection(j).difference(p))|(c.intersection(p).difference(j))|(j.intersection(p).difference(c))
print(tap_hop_2_code)

tap_hop_1_code=(c.symmetric_difference(j).symmetric_difference(p)) - tap_hop_3_code
print(tap_hop_1_code)