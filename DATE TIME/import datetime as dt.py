print(20*"=")
print("Kalkulator")
print(20*"=")

data = float(input("\nMasukkan angka : "))
operator = input("Masukkan tipe (+, -, /, * atau x, %, //, **) : ")
date = float(input("Masukkan angka : "))

if operator=='+':
    hasil = data + date 
    print (f"Hasilnya adalah : {hasil}")
    hai = input("Ada Lagi? ")
    if hai=='YES' or 'Yes' or 'yes':
            data = float(input("\nMasukkan angka : "))
            operator = input("Masukkan tipe (+, -, /, * atau x, %, //, **) : ")
            date = float(input("Masukkan angka : "))
            if operator=='+':
                hasil = data + date
                print (f"Hasilnya adalah : {hasil}")
                input("\nTekan enter untuk keluar program")
            if operator=='-':
                hasil_1 = data - date
                input("\nTekan enter untuk keluar program")
            if operator=='/':
                hasil_2 = data / date
                print (f"Hasilnya adalah : {hasil}")
                input("\nTekan enter untuk keluar program")
            if operator=='*' or 'x':
                hasil_3 = data * date
                print (f"Hasilnya adalah : {hasil}")
                input("\nTekan enter untuk keluar program")
            if operator=='%':
                hasil_4 = data % date
                print (f"Hasilnya adalah : {hasil}")
                input("\nTekan enter untuk keluar program")
            if operator=='//':
                hasil_5 = data // date
                input("\nTekan enter untuk keluar program")
            if operator== '**' or '^':
                hasil_6 = data ** date
                print (f"Hasilnya adalah : {hasil}")
                input("\nTekan enter untuk keluar program")
else:
    print("NGETIK YG BENER KONTOL")
    input("\nTekan enter untuk keluar program")

                    
if operator=='-':
    hasil = data - date 
    print (f"Hasilnya adalah : {hasil}")
    input("\nTekan enter untuk keluar program")
if operator=='/':
    hasil = data / date 
    print (f"Hasilnya adalah : {hasil}")
    input("\nTekan enter untuk keluar program")
if operator=='*' or 'x':
    hasil = data * date 
    print (f"Hasilnya adalah : {hasil}")
    input("\nTekan enter untuk keluar program")
if operator=='%':
    hasil = data % date 
    print (f"Hasilnya adalah : {hasil}")
    input("\nTekan enter untuk keluar program")
if operator=='//':
    hasil = data // date 
    print (f"Hasilnya adalah : {hasil}")
    input("\nTekan enter untuk keluar program")
if operator== '**':
    hasil = data ** date 
    print (f"Hasilnya adalah : {hasil}")
    input("\nTekan enter untuk keluar program")
else:
    print("NGETIK YG BENER KONTOL")
    input("\nTekan enter untuk keluar program")