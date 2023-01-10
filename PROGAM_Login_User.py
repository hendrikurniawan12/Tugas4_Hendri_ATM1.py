print("=======LOGIN USER=======")

username1 = "hendri"
password1 = "hujan0091"

print("")
inputusername1 =input("username :")
inputpassword1 =input("password :")

print("")
if inputusername1 == username1 :
    if inputpassword1 == password1 :
        print("berhasil login!")
    else:
        print("password salah!")
else:
    print("username salah!")

# Ada bug di programnya, coba cek lagi.
# bugnya bukan error code. tapi bug exploit user.
