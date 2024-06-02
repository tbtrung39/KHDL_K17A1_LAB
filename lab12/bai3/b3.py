import csv 
folder_path = "data\\"
while True:
    try:
        file_name = input("nhap ten file muon doc: ").strip()
        assert file_name != "","yeu cau nhap ten day du"
    except AssertionError as assertion_error:
        print(assertion_error)
    else:
        file_path = folder_path + file_name + ".csv"
        try:
            try_open_file = open(file = file_path)
        except Exception as e:
            print("loi duong dan, yeu cau nhap lai ten file")
        else:
            try_open_file.close()
            with open(file= file_path,mode= "r") as open_file:
                file_data = csv.reader(open_file)
                list_item = list(file_data)
            try:
                try_open_file = open(file="copy.dat")
            except Exception as e:
                print("tao file copt.dat")
                with open(file = "copy.dat", mode = "w") as open_file:
                    writer_file = csv.writer(open_file)
                    for item in list_item:
                        writer_file.writerow(item)
                break
            else:
                try_open_file.close()
                with open(file = "copy.dat", mode = "a") as open_file:
                    writer_file = csv.writer(open_file)
                    for item in list_item:
                        writer_file.writerow(item)
                break