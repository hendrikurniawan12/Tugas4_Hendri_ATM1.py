print("==========Progam Memasukan Max==========")

data1 = int(input("Masukkan data1 : "))
data2 = int(input("Masukkan data2 : "))
data3 = int(input("Masukkan data3 : "))

if data1 > data2 and data1 > data3 :
    print("data terbeser adalah data 1")
elif data2 > data1 and data2 > data3 :
    print("data terbesar adalah data 2")
elif data1 == data2 and data1 == data3 :
    print("semua data sama")
else:
    print("data terbesar adalah data 3")