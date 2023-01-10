print("===========================")
print("=                         =")
print("=        Tarif Parkir     =")
print("=                         =")
print("===========================")

jampertama=3500
jamselanjutnya=2000

masuk = int(input("jam masuk : "))
keluar = int(input("jam keluar : "))
jamtotal =(keluar) - (masuk)

if masuk > 12 and keluar > 12:
    print("jam keluar / masuk harus bernilai 1 - 12")
elif jamtotal <12:
    print("durasi")
elif (jamtotal <= 0):
    print("durasi : ",jamtotal+12,"jam")
    print("tarif parkir :Rp",(jampertama) + (jamtotal+12 - 1)*(jamselanjutnya))
else:
    print("durasi : ",jamtotal,"jam")
    print("tarif parkir : Rp",(jampertama) + (jamtotal- 1)*(jamselanjutnya))


