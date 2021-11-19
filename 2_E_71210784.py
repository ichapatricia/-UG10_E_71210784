suhu  = float(input("Masukan suhu tubuh anda: "))
if (suhu > 50): 
    print("Anda bukan manusia")
elif (suhu < 32):
    print("Anda kedinginan!Silahkan cari sesuatu yang hangat")
elif (suhu >= 37.5 ) and (suhu < 50):          
    print("Anda demam!Jangan bepergian ke tempat fasilitas umum")
elif (suhu > 32) and (suhu <= 37.5):
    print("Suhu anda Normal")