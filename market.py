#  Aplikasi Market

#Stock
apple_stock = 7
orange_stock = 7
grape_stock = 6

apple = int(input("Masukkan jumlah apel: "))

while apple > apple_stock :
    print("Jumlah yang dimasukkan terlalu banyak")
    print(f"Stock apel tinggal {apple_stock}")
    apple = int(input("Masukkan jumlah apel: "))
    
    
orange = int(input("Masukkan jumlah jeruk: "))

while orange > orange_stock :
    print("Jumlah yang dimasukkan terlalu banyak")
    print(f"Stock jeruk tinggal {orange_stock}")
    orange = int(input("Masukkan jumlah jeruk: "))

grape = int(input("Masukkan jumlah anggur: "))

while grape > grape_stock :
    print("Jumlah yang dimasukkan terlalu banyak")
    print(f"Stock anggur tinggal {grape_stock}")
    grape =int(input("Masukkan jumlah anggur: "))

#Price
apple_price = apple * 10_000
orange_price = orange * 15_000
grape_price = grape * 20_000

total = apple_price + orange_price + grape_price

print("\nDetail Belanja")

print(f"\nApel : {apple} x 10000 = {apple_price}")
print(f"Jeruk : {orange} x 15000 = {orange_price}")
print(f"Apel : {grape} x 20000 = {grape_price}")

print(f"\nTotal : {total}")

while True:
    money = int(input("\nMasukkan jumlah uang : "))

    if money < total:
        print("\nTransaksi anda dibatalkan")
        print(f"uang anda kurang sebesar {total - money}")
    elif money == total:
        print("\nUang anda sudah pas")
        print("Terima kasih")
    else :
        print("\nTerima kasih")
        print(f"Uang kembali anda sebesar: {money - total}")