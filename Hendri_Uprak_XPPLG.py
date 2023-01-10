print("===== APP PEMESANAN FOOD CORNER BPI ===== ")     #*output judul

option=0
print("1. Makanan berat [potongan Rp. 2000 All item!")#*input bnayak perulangan
print("2. Makanan ringan")
print("3. minuman")
option =int(input("mau beli berapa item?"))
if option==1:
    print("potongan raharga 2000")
    makanan1=input("makan berat:")#input
    harga1=input("harga item:")#input
    potonganharga = 2000
    hasil1 = harga1-potonganharga

for i in range(option):   #*di dalam perulangan:
    i+=1#nomer
