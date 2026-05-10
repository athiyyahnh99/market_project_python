#  Aplikasi Market
# Nama : Athiyyah Nisrina Husna


fruit = [
    {"stock": 10, "product": "Apel", "price": 10_000},
    {"stock": 10, "product": "Jeruk", "price": 15_000},
    {"stock": 10, "product": "Anggur", "price": 20_000},
]
def view_menu():# Main menu
    print("\n=== Selamat Datang di Pasar Buah ===")
    print("\nList Menu: ")
    print("1. Menampilkan daftar Buah")
    print("2. Menambah Buah")
    print("3. Menghapus Buah")
    print("4. Membeli Buah")
    print("5. Exit Program")
    choice = input("Masukkan angka menu yang ingin dijalankan: ")
    return choice

def get_product():
    print("\nDaftar Buah")
    print(f"{"Index":<7}|{"Nama":<10}|{"Stock":<5}|{"Harga":<16}")
    for idx in range(len(fruit)):
        print (f"{idx:<7}|{fruit[idx]["product"]:<10}|{fruit[idx]["stock"]:<5}|{fruit[idx]["price"]:<16}")

def add_product(product_name, product_stock = 0,product_price = 0) : # parameter yg mempunyai default ditaruh diakhir
    product = {
        "product" : product_name,
        "stock" : product_stock,
        "price" : product_price
    }
    print(product)
    confirm = input("yakin untuk menambah produk (y/n)?")
    if confirm.lower() == "y":
        fruit.append(product)
        print("Produk berhasil ditambahkan!")
    else:
        print("Produk batal ditambahkan")
    
    get_product()
    
    
def delete_product():
    get_product()
    delete_fruit= int(input("Masukkan index buah yang ingin dihapus: "))
    if 0 <= delete_fruit < len(fruit):
        deleted = fruit.pop(delete_fruit)
        print(f"'{deleted['product']}' berhasil dihapus!")
        get_product()
    else: 
        print("index tidak valid!")
    
    
def add_to_cart(cart):
    get_product()
    buy_fruit = int(input("Masukkan index buah yang ingin dibeli : "))
    buy_qty = int(input("Masukkan jumlah yang ingin dibeli    : "))
    if not (0 <= buy_fruit < len(fruit)):
        print("Index tidak valid!")
        return
    # Cek stock
    if buy_qty > fruit[buy_fruit]["stock"]:
        print(f"Stock tidak cukup, stock {fruit[buy_fruit]['product']} tinggal {fruit[buy_fruit]['stock']}")
        return

    # Masuk ke cart
    cart.append({
        "product": fruit[buy_fruit]["product"],
        "qty":     buy_qty,
        "price":   fruit[buy_fruit]["price"]
    })
    show_cart(cart)
    
def show_cart(cart):
    print("\nIsi Cart")
    print(f"{'Nama':<10}| {'Qty':<5}| {'Harga'}")
    for item in cart:
        print(f"{item['product']:<10}| {item['qty']:<5}| {item['price']}")


def checkout(cart):
    total_harga = 0
    for item in cart:
        total_harga += item["qty"] * item["price"]

    # Tampilkan daftar belanja
    print("\nDaftar Belanja")
    print(f"{'Nama':<10}| {'Qty':<5}| {'Harga':<10}| {'Total Harga'}")
    for item in cart:
        print(f"{item['product']:<10}| {item['qty']:<5}| {item['price']:<10}| {item['qty'] * item['price']}")

    print(f"Total Yang Harus Dibayar : {total_harga}")
    
    while True:
        bayar = int(input("Masukkan jumlah uang: Rp"))
        if bayar >= total_harga:
            break
        print(f"Uang kurang! Total: Rp{total_harga:,}, uang kamu: Rp{bayar:,}")

    print("Terima kasih sudah berbelanja!")
    print(f"Uang kembali: Rp{bayar - total_harga:,}")
    
def buy_product():
    cart = []
    while True:
        add_to_cart(cart)
        cont = input("\nMau beli yang lain? (y/n): ")
        if cont.lower() != "y":
            break
    checkout(cart)




running =True
while running :
    choice = view_menu()
    if choice == "1": #Menampilkan daftar buah
        get_product()
        
    elif choice == "2": #Menambah buah
        print("\nTambah Daftar Buah")
        product_name = input("Masukkan nama buah: ")
        product_stock = int(input("Masukkan stok buah: "))
        product_price = int(input("Masukkan harga buah: "))
        add_product(product_name,product_stock,product_price)
        
    elif choice == "3": #Menghapus buah
       delete_product()
            
    elif choice == "4": # membeli buah
        buy_product()
  
    elif choice == "5":
        running = False
    else:
        print("\nPilihan tidak ada di dalam menu\n")    