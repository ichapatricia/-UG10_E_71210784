siswa= input("Masukan daftar siswa: ")
siswa_kapital= siswa.title()
array_siswa=siswa_kapital.split(", ")

print(array_siswa)
siswa_2= input("Masukan nama siswa yang ingin ditambahkan: ")
siswa_2_kapital= siswa_2.title()
array_siswa_2= siswa_2_kapital.split()

if array_siswa[0] == siswa_2_kapital: 
    print("Siswa atas nama", siswa_2_kapital.upper(),"sudah berada dalam daftar siswa")
elif array_siswa[1] == siswa_2_kapital:
    print("Siswa atas nama", siswa_2_kapital.upper(),"sudah berada dalam daftar siswa")
elif array_siswa[2] == siswa_2_kapital:
    print("Siswa atas nama", siswa_2_kapital.upper(),"sudah berada dalam daftar siswa")
else:
    siswa_2_kapital= siswa_2.upper()
    array_siswa.append(siswa_2_kapital)
    print("Hasil penambahan daftar nama siswa",array_siswa)
