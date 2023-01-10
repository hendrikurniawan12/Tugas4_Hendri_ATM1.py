print(" ==== PROGAM NILAI KELAS X-PPLG ====")
rata_kelas=0
siswa= int(input("input berapa nilai?"))

for i in range(siswa):
    i+=1
    print(i)
    nama_siswa=input("nama siswa :")
    nilai_tugas=input("nilai tugas :")
    nilai_harian=input("nilai harian :")
    nilai_pts=input("nilai pts :")
    nilai_pas=input("nilai pas :")
print("----------------------------")
print(namasiswa)
jumlah_nilai =nilaitugas + nilaiharian+ nilaipas+ nilaipts
print(jumlah_nilai)
rata_nila= jumlah_nilai/4
print("rata-rata nilai:",rata_nila)
print()
rata_kelas+= (rata_kelas+rata_nila)/siswa
print("rata rata kelas:",rata_kelas)
