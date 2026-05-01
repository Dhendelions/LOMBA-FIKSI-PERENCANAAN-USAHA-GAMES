print("\nMANUPULASI STRING")
print("====================")

#1. Menyambung String
print("\n1.) Menyambung String")

nama = 'Crissencio'
nama_1 = 'Dheni'
nama_2 = 'S.'
nama_3 = 'Cristiano'
nama_4 = 'Ronaldo'

nama_lengkap = nama + " " + nama_1 + " " + nama_2
print(f"Nama saya adalah {nama_lengkap}")
nama_asli = nama_3 + " " + nama_4 
print(f"Nama saya adalah {nama_asli}")

#2. Menghitung panjang string
print("\n2.) Menghitunug Panjang String")

long = len(nama_lengkap)
print(f"Panjang dari {nama_lengkap} adalah {long}")
lang = len(nama_asli)
print(f"Panjang dari {nama_asli} adalah {lang}")

#3. Operator String

print("\n3.) Operator String")
print("\na.) Mengetahui char ada apa tidak")

dheni = 'Dheni'
status = dheni in nama_lengkap
print(f"Status {dheni} dalam {nama_lengkap} adalah {status}")
dhenu = 'dheni'
statas = dhenu in nama_lengkap
print(f"Status {dhenu} dalam {nama_lengkap} adalah {statas}")

ronal = 'Ronaldo'
statys = ronal not in nama_asli
print(f"Status {ronal} dalam (NOT IN ) {nama_asli} adalah {statys}")
ronil = 'ronaldo'
statts = ronil not in nama_asli
print(f"Status {ronil} dalam (NOT IN) {nama_asli} adalah {statts}")

print("\nb.) Mengulang String")
print('me'*10)
print(10*'woi ')

print("\nc.) Indexing")
print("Penjelasan : index dimulai dari 0,1,2,3 bukan dari 1,2,3,4")
print(f"Index ke-10 dari {nama_lengkap} adalah :", nama_lengkap[10])
print(f"Index ke-9 dari {nama_lengkap} adalah :", nama_lengkap[9])
print(f"Index ke-10 dari {nama_asli} adalah :", nama_asli[10])
print(f"Index ke-9 dari {nama_asli} adalah :", nama_asli[9])

print("\nd.) Item Kecil & Besar")
print("*KECIL*")
print(f"Nilai terkecil dari {nama_lengkap} adalah :", min(nama_lengkap))
print(f"Nilai terkecil dari {nama_asli} adalah :", min(nama_asli))
print("*BESAR*")
print(f"Nilai terbesar dari {nama_lengkap} adalah :", max(nama_lengkap))
print(f"Nilai terbesar dari {nama_asli} adalah :", max(nama_asli))

print("\nASCII CODE")
data = ord(" ")
print(f"ASCII-CODE dari spasi adalah : {str(data)}")
date = ord("t")
print(f"ASCII-CODE dari t adalah : {str(date)}")

print("\n4.) Operator Dalam Bentuk Method")
jumlah = nama_lengkap.count("s")
jumlih = nama_asli.count("a")
print(f"Jumlah huruf S dalam {nama_lengkap} adalah : {jumlah}")
print(f"Jumlah huruf S dalam {nama_asli} adalah : {jumlih}")

print = input("\nTekan enter untuk keluar")