print(" ==== Kalkulator Akar dan Pangkat ==== ")
print("Pilihan menu:")
print("1. Pangkat 2 (kuadrat)")
print("2. Pangkat 3 (kubik)")
print("3. Akar Kuadrat")
menu = int(input("Masukan menu yang anda pilih: "))
if menu == 1:
        pangkat2= int(input(" Masukan bilangan yang ingin dipangkat: "))
        hasil= pangkat2 ** 2
        print("Hasil dari pemangkatan bilangan" , pangkat2 , "dengan 2 (kuadrat) adalah", hasil)
elif menu == 2:
        pangkat3= int(input("Masukan bilangan yang ingin dipangkat: ")) 
        hasil= pangkat3 ** 3
        print("Hasil dari pemangkatan bilangan", pangkat3, " dengan 3 (kubik) adalah", hasil )
elif  menu == 3:
     akar= int(input("Masukan bilangan yang ingin diakarkan: "))  
     hasil= akar ** 0.5
     print("Hasil dari akar kuadrat dari", akar, "adalah")
else: 
    print("Pilihan menu yang dimasukan tidak sesuai")    