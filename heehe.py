i=1
jumlah=0
for i in range(1,6,1):
    jumlah=jumlah+i

    print("memanggil",i,"kali")

angka=int(input("mau memanggil berapa kali?:"))
for i in range(1,angka+1):
    jumlah=jumlah+i
    print("memanggil",i,"kali")