print("SELAMAT DATANG DI ATM SAYA")
print("pilih opting")
print("1. check uang saya")
print("2. ambil uang saya")
print("3. tabung uang saya")
option=int(input("silahkan pilih option :"))
if option==1:
    print("uang kamu berjumlah 1.000.000")
elif option==2:
    print("uang kamu berjumlah 1.000.000, mau ambil berapa?")
    print("1. rp.100.000")
    print("2. rp.200.000")
    uang_kamu=200000
    option2=int(input("option :"))
    if option2==1:
        hasil=uang_kamu-100000
        print("uang kamu sekarang berjumlah :",hasil)
    elif option2==2:
        hasil2=uang_kamu-200000
        print("uang kamu sekarang berjumlah :",hasil2)
    else:
        print("keyword anda salah!")
elif option==3:
    uang_kamu=200000
    print("uang berjumlah rp.200.000, mau nabung berapa?")
    option3=int(input("masukkan jumlah uang :"))
    hasil3=uang_kamu+option3
    print("jumlah uang kamu sekarang adalah",hasil3)
else:
    print("keyword anda salah, mohon coba lagi!")