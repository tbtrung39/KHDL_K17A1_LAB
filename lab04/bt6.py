so = input("Nhập số: ")
chuyen_doi_so = {
    '0' : "không",
    '1' : " một",
    '2' : " hai",
    '3' : " ba",
    '4' : "bốn",
    '5' : "năm",
    '6' : "sáu",
    '7' : "bảy",
    '8' : "tám",
    '9' : "chín"
}

for i in so:
    if i in chuyen_doi_so:
        print(chuyen_doi_so[i], end =" ")