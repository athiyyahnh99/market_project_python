#  Aplikasi Market
# Nama : Athiyyah Nisrina Husna

#Stock
stock = [10,10,10]
#Price
price = [10_000, 15_000, 20_000]

print("=== Selamat Datang di Pasar Buah ===")

print("\nList Menu: ")
print("1. Menampilkan daftar Buah")
print("2. Menambah Buah")
print("3. Menghapus Buah")
print("4. Membeli Buah")
print("5. Exit Program")


fruit = [[10,"Apple",10_000],
         [10,"Orange",15_000],
         [10,"Grape",20_000]]

while True :
    choice = input("Masukkan angka menu yang dijalankan : ")
    if choice == "1": #Menampilkan daftar buah
        print("Daftar Buah")
        i = 0
        for i in range(len(fruit)):
            print (f"{i:<6}{fruit[i+0][1]:<10}{fruit[i+0][2]:<12}{fruit[i+0][2]}")
    elif choice == "2": #Menambah buah
        add_fruit = input(print("Masukkan nama buah: "))
        add_stock = int(input(print("Masukkan stock buah: ")))
        add_price = int(input(print("Masukkan harga buah: ")))
        
        fruit.append([add_fruit,add_stock,add_price]) 
        print(fruit)
        #i = 0
        #for i in range(len(fruit)):
            #print (f"{i:<6}{fruit[i+0][1]:<10}{fruit[i+0][2]:<12}{fruit[i+0][2]}") 
        
        
        
        



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

total = apple_price + orange_price + grape_price

print("\nDetail Belanja")

print(f"\nApel : {apple} x 10000 = {apple * apple_price}")
print(f"Jeruk : {orange} x 15000 = {orange * orange_price}")
print(f"Apel : {grape} x 20000 = {grape * grape_price}")

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