print("====================================================================================")
print("DATE TIME")

import datetime as dt

waktu = dt.date.today()
nama = str(input("Masukkan Nama \t: "))
lahir_1 = int(input("Year of birth \t: "))
lahir_2 = int(input("Month of birth \t: "))
lahir_3 = int(input("Date of birth \t: "))

lahir = dt.date(lahir_1, lahir_2, lahir_3 )
print("Welcome", nama,", Youre born at", lahir)

umur = waktu - lahir
umur_1 = umur.days // 365
print("You're Age :", umur_1, "Years Old")

print("\nWelcome", nama, ", Signed At", waktu)

print("\n====================================================================================")
print("\nChoose one number of three things")
print("\n1.) Age Guesser \n2.) Day Guesser When You Was Born \n3.) Day Conversion")
work = int(input("What's you're needs? (answer via numbers): "))
print("Okey you're choose number", work)

if work==1:
    print("You Chose a great option, now i gonna help you")
    print("\nWhen you're or you're friends born?")
    lahir_4 = int(input("Year of birth \t: "))
    lahir_5 = int(input("Month of birth \t: "))
    lahir_6 = int(input("Date of birth \t: "))

    lahir_a = dt.date(lahir_4, lahir_5, lahir_6 )
    print("You born at", lahir_a)
    
    umur_a = waktu - lahir_a
    umur_a1 = umur_a.days // 365
    print("You're age is", umur_a1, "Years old")

    benar = str(input("That's correct? \n(YES/NO) : "))

    if benar=='YES':
        print("Thank you for you partisipation")
        input("Press enter for close this program")
    else:
        print("Im sorry")
        salah = str(input("Give me a suggestion :"))
        print("TAHNKS")
        input("Press enter for close this program")

if work==2:
    print("Okeyy this option it's so great for you")
    print("\nNow i gonna help you in this problem")

    print("\nWhen you're or you're friends born?")
    lahir_7 = int(input("Year of birth \t: "))
    lahir_8 = int(input("Month of birth \t: "))
    lahir_9 = int(input("Date of birth \t: "))
    lahir_b = dt.date(lahir_7,lahir_8,lahir_9)

    print("Okeyy this date it's", lahir_b)
    print(f"That's day when you born is : {lahir_b:%A}")
    
    benar_a = str(input("\nThat's correct? \n(YES/NO) : "))
    if benar_a=='YES':
        print("Thank you for the partisipation")
        input("Press enter for close this program")
    else:
        print("I'm sorry")
        maaf = input("Give me a suggestion please : ")
        print("Thank you for the partisipation")
        input("Press enter for close this program")

if work==3:
    print("Okeyy i gonna help you today")
    date = dt.date.today()
    print("\nThis date it's", date)
    hari = (f"{date:%A}")
    print(f"And the day is : ", hari)

    indeks = {
        'senin': 0,
        'selasa': 1,
        'rabu': 2,
        'kamis':3,
        'jumat': 4,
        'sabtu': 5,
        'minggu': 6,    
    }

    tomorow_1 = str(input("Enter the current day : ")) 
    tomorow = int(input("How many days will you add : "))
    print(f"\nYou chose are {tomorow_1} and change it to {tomorow} days")

    if tomorow_1=='monday':
        tomorow_1 = 0
        hasil = (0 + tomorow) %7
        if hasil==0:
            print("That's day is : MONDAY")
            input("Press enter for close this program")
        if hasil==1:
            print("That's day is : TUESDAY")
            input("Press enter for close this program")
        if hasil==2:
            print("That's day is : WEDNESDAY")
            input("Press enter for close this program")
        if hasil==3:
            print("That's day is : THURSDAY")
            input("Press enter for close this program")
        if hasil==4:
            print("That's day is : FRIDAY")
            input("Press enter for close this program")
        if hasil==5:
            print("That's day is : SATURDAY")
            input("Press enter for close this program")
        if hasil==6:
            print("That's day is : SUNDAY")
            input("Press enter for close this program")

    if tomorow_1=='tuesday':
        tomorow_1 = 1
        hasil = (1 + tomorow) %7
        if hasil==0:
            print("That's day is : MONDAY")
            input("Press enter for close this program")
        if hasil==1:
            print("That's day is : TUESDAY")
            input("Press enter for close this program")
        if hasil==2:
            print("That's day is : WEDNESDAY")
            input("Press enter for close this program")
        if hasil==3:
            print("That's day is : THURSDAY")
            input("Press enter for close this program")
        if hasil==4:
            print("That's day is : FRIDAY")
            input("Press enter for close this program")
        if hasil==5:
            print("That's day is : SATURDAY")
            input("Press enter for close this program")
        if hasil==6:
            print("That's day is : SUNDAY")
            input("Press enter for close this program")

    if tomorow_1=='wednesday':
        tomorow_1 = 2
        hasil = (2 + tomorow) %7
        if hasil==0:
            print("That's day is : MONDAY")
            input("Press enter for close this program")
        if hasil==1:
            print("That's day is : TUESDAY")
            input("Press enter for close this program")
        if hasil==2:
            print("That's day is : WEDNESDAY")
            input("Press enter for close this program")
        if hasil==3:
            print("That's day is : THURSDAY")
            input("Press enter for close this program")
        if hasil==4:
            print("That's day is : FRIDAY")
            input("Press enter for close this program")
        if hasil==5:
            print("That's day is : SATURDAY")
            input("Press enter for close this program")
        if hasil==6:
            print("That's day is : SUNDAY")
            input("Press enter for close this program")

    if tomorow_1=='thursday':
        tomorow_1 = 3
        hasil = (3 + tomorow) %7
        if hasil==0:
            print("That's day is : MONDAY")
            input("Press enter for close this program")
        if hasil==1:
            print("That's day is : TUESDAY")
            input("Press enter for close this program")
        if hasil==2:
            print("That's day is : WEDNESDAY")
            input("Press enter for close this program")
        if hasil==3:
            print("That's day is : THURSDAY")
            input("Press enter for close this program")
        if hasil==4:
            print("That's day is : FRIDAY")
            input("Press enter for close this program")
        if hasil==5:
            print("That's day is : SATURDAY")
            input("Press enter for close this program")
        if hasil==6:
            print("That's day is : SUNDAY")
            input("Press enter for close this program")

    if tomorow_1=='friday':
        tomorow_1 = 4
        hasil = (4 + tomorow) %7
        if hasil==0:
            print("That's day is : MONDAY")
            input("Press enter for close this program")
        if hasil==1:
            print("That's day is : TUESDAY")
            input("Press enter for close this program")
        if hasil==2:
            print("That's day is : WEDNESDAY")
            input("Press enter for close this program")
        if hasil==3:
            print("That's day is : THURSDAY")
            input("Press enter for close this program")
        if hasil==4:
            print("That's day is : FRIDAY")
            input("Press enter for close this program")
        if hasil==5:
            print("That's day is : SATURDAY")
            input("Press enter for close this program")
        if hasil==6:
            print("That's day is : SUNDAY")
            input("Press enter for close this program")

    if tomorow_1=='saturday':
        tomorow_1 = 5
        hasil = (5 + tomorow) %7
        if hasil==0:
            print("That's day is : MONDAY")
            input("Press enter for close this program")
        if hasil==1:
            print("That's day is : TUESDAY")
            input("Press enter for close this program")
        if hasil==2:
            print("That's day is : WEDNESDAY")
            input("Press enter for close this program")
        if hasil==3:
            print("That's day is : THURSDAY")
            input("Press enter for close this program")
        if hasil==4:
            print("That's day is : FRIDAY")
            input("Press enter for close this program")
        if hasil==5:
            print("That's day is : SATURDAY")
            input("Press enter for close this program")
        if hasil==6:
            print("That's day is : SUNDAY")
            input("Press enter for close this program")

    if tomorow_1=='sunday':
        tomorow_1 = 6
        hasil = (6 + tomorow) %7
        if hasil==0:
            print("That's day is : MONDAY")
            input("Press enter for close this program")
        if hasil==1:
            print("That's day is : TUESDAY")
            input("Press enter for close this program")
        if hasil==2:
            print("That's day is : WEDNESDAY")
            input("Press enter for close this program")
        if hasil==3:
            print("That's day is : THURSDAY")
            input("Press enter for close this program")
        if hasil==4:
            print("That's day is : FRIDAY")
            input("Press enter for close this program")
        if hasil==5:
            print("That's day is : SATURDAY")
            input("Press enter for close this program")
        if hasil==6:
            print("That's day is : SUNDAY")
            input("Press enter for close this program")

