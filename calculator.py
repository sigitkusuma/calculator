from Operasi.operasiBilangan import penjumlahan as jumlah, pengurangan as kurang, info, pembagian as bagi, perkalian as kali

bil1 = float(input('Masukan Angka : '))
bil2 = float(input('Masukan Angka : '))

operasi = input('''Masukan operasi bilangan  
+ Operasi 
- Pengurangan  
/ Pembagian 
x Perkalian  ''')

if operasi == "+":
    print(info())
    print(jumlah(bil1, bil2))
elif operasi == "-":
    print(info())
    print(kurang(bil1, bil2))
elif operasi == "/":
    print(info())
    print(bagi(bil1, bil2))
elif operasi == "x":
    print(info())
    print(kali(bil1, bil2))

else:print("Not Found")