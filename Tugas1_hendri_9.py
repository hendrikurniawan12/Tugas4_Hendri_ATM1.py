#kasir
print("=========PRONGAM KASIR 3 BARANG==========")

Barang1 = input("barng1 :")
harga1 = int(input("harga :"))
Barang2 = input("barang2 :")
harga2 = int(input("harga2 :"))
Barang3 = input("barang3 :")
harga3 = int(input("harga3 :"))
uang1 = int(input("uang pelanggan :"))


print("penjual pembeli")
print("1",Barang1,"RP",harga1)
print("2",Barang2,"RP",harga2)
print("3",Barang3,"RP",harga3)

total = int(harga1)+ (harga2) + (harga3)
total2 = total-(total*20/100)

print("total baramg :", total)

print("anda mendapat diskon 20%")
print("total yang harus di bayar pelanggan : Rp. ",total-(total*20/100))

print(f"uang pelanggan {uang1}")
print(f"kembalian : {uang1-total2}")


print("TERIMAKASIH BANYAK")