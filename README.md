# UAS-bahasa-pemrograman
## Dictionary Menu:

### menu adalah sebuah dictionary yang berisi daftar menu makanan/minuman beserta harganya. Setiap item diwakili oleh nama makanan sebagai kunci dan harganya sebagai nilai.
## Fungsi tampilkan_menu():

### Fungsi ini bertugas untuk menampilkan seluruh menu makanan/minuman beserta harganya ke layar.
## Fungsi hitung_total(pesanan):

### Fungsi ini menerima daftar pesanan sebagai argumen dan mengembalikan total harga dari pesanan tersebut berdasarkan menu yang ada.
## Fungsi tampilkan_struk(pesanan, total_harga):

### Fungsi ini menerima daftar pesanan dan total harga sebagai argumen, lalu menampilkan struk pembelian berisi daftar pesanan beserta total harga.
## Fungsi main():

### Fungsi utama yang akan dijalankan. Pertama, ia menampilkan menu menggunakan tampilkan_menu().Selanjutnya, menggunakan loop while untuk meminta pengguna memilih makanan/minuman. Loop ini terus berjalan hingga pengguna memilih untuk selesai belanja dengan mengetik 'selesai'. Saat pengguna memasukkan pesanan, program akan mengecek apakah pesanan tersebut ada di menu atau tidak. Jika ada, pesanan akan ditambahkan ke dalam list pesanan. Setelah selesai belanja, program akan menghitung total harga pesanan menggunakan hitung_total(pesanan) dan menampilkan struk pembelian menggunakan tampilkan_struk(pesanan, total_harga). if __name__ == "__main__":

# link video dokumentasi: https://youtu.be/e0V_050SyAY?si=CN_eK0cPdJBzxmc7