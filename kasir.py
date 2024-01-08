menu = {
    'Nasi Goreng': 15000,
    'Mie Goreng': 12000,
    'Ayam Goreng': 18000,
    'Es Teh Manis': 5000,
    'Jus Jeruk': 8000,
    'Air Mineral': 3000
}

def tampilkan_menu():
    print("Menu Makanan/Minuman:")
    print("=====================")
    for item, harga in menu.items():
        print(f"{item}: Rp {harga}")

def hitung_total(pesanan):
    total = 0
    for item in pesanan:
        if item in menu:
            total += menu[item]
    return total

def tampilkan_struk(pesanan, total_harga):
    print("\n--- Struk Pembelian ---")
    print("Pesanan:")
    for item in pesanan:
        print(f"- {item}: Rp {menu[item]}")
    print(f"Total harga: Rp {total_harga}")
    print("-----------------------")

def main():
    tampilkan_menu()

    pesanan = []
    lanjut = True
    while lanjut:
        pilihan = input("\nPilih makanan/minuman (atau ketik 'selesai' untuk selesai belanja): ")
        if pilihan.lower() == 'selesai':
            lanjut = False
        elif pilihan in menu:
            pesanan.append(pilihan)
        else:
            print("Maaf, makanan/minuman tidak tersedia.")

    total_harga = hitung_total(pesanan)
    tampilkan_struk(pesanan, total_harga)

if __name__ == "__main__":
    main()
