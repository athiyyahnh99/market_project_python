#  Aplikasi Market
# Nama : Athiyyah Nisrina Husna


fruit = [
    {"stock": 10, "product": "Apel", "price": 10_000},
    {"stock": 10, "product": "Jeruk", "price": 15_000},
    {"stock": 10, "product": "Anggur", "price": 20_000},
]

print(fruit)

running =True
while running :
    # Main Menu
    print("\n=== Selamat Datang di Pasar Buah ===")

    print("\nList Menu: ")
    print("1. Menampilkan daftar Buah")
    print("2. Menambah Buah")
    print("3. Menghapus Buah")
    print("4. Membeli Buah")
    print("5. Exit Program")
    choice = input("Masukkan angka menu yang ingin dijalankan: ")
    
    if choice == "1": #Menampilkan daftar buah
        print("\nDaftar Buah")
        print(f"{"Index":<7}|{"Nama":<10}|{"Stock":<5}|{"Harga":<16}")
        for idx in range(len(fruit)):
            print (f"{idx:<7}|{fruit[idx]["product"]:<10}|{fruit[idx]["stock"]:<5}|{fruit[idx]["price"]:<16}")
        
    elif choice == "2": #Menambah buah
        while True:
            add_fruit = input("Masukkan nama buah: ")
            add_stock = int(input("Masukkan stock buah: "))
            add_price = int(input("Masukkan harga buah: "))
            
            plus_fruit = [{"stock": add_stock, "product": add_fruit, "price": add_price}]
            fruit.append(plus_fruit)
            
            confirm_msg = input("Lanjut tambah buah (yes:jika lanjut)?: ")
            if confirm_msg.lower() != "yes":
                print("Tambah buah selesai")
                
            print(f"{"Index":<7}|{"Nama":<10}|{"Stock":<5}|{"Harga":<16}")
            for idx in range(len(fruit)):
                print (f"{idx:<7}|{fruit[idx]["product"]:<10}|{fruit[idx]["stock"]:<5}|{fruit[idx]["price"]:<16}")
            break
        
    elif choice == "3": #Menghapus buah
        print("\nDaftar Buah")
        print(f"{"Index":<7}|{"Nama":<10}|{"Stock":<5}|{"Harga":<16}")
        for idx in range(len(fruit)):
            print (f"{idx:<7}|{fruit[idx]["product"]:<10}|{fruit[idx]["stock"]:<5}|{fruit[idx]["price"]:<16}")
        delete_fruit= int(input("Masukkan index buah yang ingin dihapus: "))
        fruit.pop(delete_fruit)
        
        print(f"{"index":<6}{"Nama":<10}{"Stock":<12}{"Harga"}")
        for idx in range(len(fruit)):
            print (f"{idx:<7}|{fruit[idx]["product"]:<10}|{fruit[idx]["stock"]:<5}|{fruit[idx]["price"]:<16}")
            
    elif choice == "4": # membeli buah
        cart = []
        while True:
            print("\nDaftar Buah")
            print(f"{'Index':<7}| {'Nama':<10}| {'Stock':<7}| {'Harga'}")
            for idx in range(len(fruit)):
                print(f"{idx:<7}| {fruit[idx]['product']:<10}| {fruit[idx]['stock']:<7}| {fruit[idx]['price']}")

            buy_fruit = int(input("Masukkan index buah yang ingin dibeli : "))

            buy_qty = int(input("Masukkan jumlah yang ingin dibeli    : "))

            # Cek stock
            if buy_qty > fruit[buy_fruit]["stock"]:
                print(f"Stock tidak cukup, stock {fruit[buy_fruit]['product']} tinggal {fruit[buy_fruit]['stock']}")
                continue

            # Masuk ke cart
            cart.append({
                "product": fruit[buy_fruit]["product"],
                "qty":     buy_qty,
                "price":   fruit[buy_fruit]["price"]
            })

            # Tampilkan isi cart
            print("\nIsi Cart")
            print(f"{'Nama':<10}| {'Qty':<5}| {'Harga'}")
            for item in cart:
                print(f"{item['product']:<10}| {item['qty']:<5}| {item['price']}")

            cont = input("Mau beli yang lain? (ya/tidak) : ")
            if cont.lower() != "ya":
                break
            

        # Hitung total belanja
        total_harga = 0
        for item in cart:
            total_harga += item["qty"] * item["price"]

        # Tampilkan daftar belanja
        print("\nDaftar Belanja")
        print(f"{'Nama':<10}| {'Qty':<5}| {'Harga':<10}| {'Total Harga'}")
        for item in cart:
            print(f"{item['product']:<10}| {item['qty']:<5}| {item['price']:<10}| {item['qty'] * item['price']}")

        print(f"Total Yang Harus Dibayar : {total_harga}")

        # Input uang,minta ulang kalau kurang dan tampilkan kembalian
        while True:
            bayar = int(input("Masukkan jumlah uang : "))
            if bayar >= total_harga:
                break
            print(f"Uang kurang! Total belanja {total_harga}, uang kamu {bayar}")

        print("Terima kasih")
        print(f"Uang kembali anda : {bayar - total_harga}")

        # Kurangi stock buah yang dibeli
        for item in cart:
            for buah in fruit:
                if buah["product"] == item["product"]:
                    buah["stock"] -= item["qty"]
                    
    elif choice == "5":
        break
        

        
     
            
    
        
    
        
        
        
        



