print("## Program Python Menghitung Gaji Karyawan ##")
print("====================================")
print("")

Nama = input("Nama Karyawan: ")
Golongan = input("Golongan: ")
JamKerja = int(input("Jumlah jam kerja: "))

if (Golongan == "A"):
  Gaji = JamKerja*5000
elif (Golongan == "B"):
  Gaji = JamKerja*7000
elif (Golongan == "C"):
  Gaji = JamKerja*8000
elif (Golongan == "D"):
  Gaji = JamKerja*10000

if (JamKerja) > 48:
  Gaji = Gaji + ((JamKerja - 48)*4000)

print(Nama, "menerima upah Rp.", Gaji, "per minggu")