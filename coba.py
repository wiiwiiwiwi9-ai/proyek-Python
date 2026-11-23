produk_atasan = [
    {
        "nama": "kaos polos",
        "kategori": "atasan",
        "harga": 60000,
        "stok": 35
    },
    {
        "nama": "kemeja flanel",
        "kategori": "atasan",
        "harga": 100000,
        "stok": 20
    }
]

produk_bawahan = [
    {
        "nama": "celana jeans",
        "kategori": "bawahan",
        "harga": 160000,
        "stok": 15
    },
    {
        "nama": "celana training",
        "kategori": "bawahan",
        "harga": 120000,
        "stok": 10
    }
]

produk_aksesoris = [
    {
        "nama": "topi",
        "kategori": "aksesoris",
        "harga": 30000,
        "stok": 20
    },
    {
        "nama": "jam tangan",
        "kategori": "aksesoris",
        "harga": 80000,
        "stok": 10
    }
]

semua_produk = produk_atasan + produk_bawahan + produk_aksesoris

def tampilkan_produk(daftar_produk):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("       daftar produk       ")
    nomor = 1

    for p in daftar_produk:
        print(f"|nomor {nomor}|")
        print("nama     :", p["nama"])
        print("kategori :", p["kategori"])
        print("harga    : rp", p["harga"])
        print("stok     :", p["stok"])
        print("_____________________________")
        nomor += 1

while True:
    print("================================")
    print("          FASHION STORE")
    print("================================")
    print("1. |  Tampilkan Daftar Produk  |")
    print("2. |        Cari Produk        |")
    print("3. |   Tambahkan ke Keranjang  |")
    print("4. |       Lihat Keranjang     |")
    print("5. |          Checkout         |")
    print("6. |     Riwayat Transaksi     |")
    print("7. |           Keluar          |")
    print("================================")
   
    pilihan = int(input("pilih menu di atas: "))
    if pilihan == 1:
        tampilkan_produk(semua_produk)
    elif pilihan == 2:
        print("________~~~~~~________","\n   pencarian produk:")
        print("1.| atasan", "\n2.| bawahan", "\n3.| aksesoris")
        kategori = input("Masukkan kategori produk: ")

        ditemukan = False

        for p in semua_produk:
            if p["kategori"] == kategori:
                print("___daftar produk___")
                print("nama     :", p["nama"])
                print("kategori :", p["kategori"])
                print("harga    : Rp", p["harga"])
                print("stok     :", p["stok"])
                print("-----------------------------")
                ditemukan = True

        if ditemukan == False:
            print("Kategori produk tidak tersedia")