nama = "Heldi Irwansah"

# ubah ke huruf kecil biar konsisten
nama = nama.lower()

# ubah jadi list lalu urutkan
huruf = list(nama)
huruf.sort()

cari = 'a'

# proses binary search
kiri = 0
kanan = len(huruf) - 1
ketemu = -1

while kiri <= kanan:
    tengah = (kiri + kanan) // 2
    
    if huruf[tengah] == cari:
        ketemu = tengah
        break
    elif huruf[tengah] < cari:
        kiri = tengah + 1
    else:
        kanan = tengah - 1

print("Data setelah diurutkan:", huruf)

if ketemu != -1:
    print("Huruf", cari, "ditemukan di index", ketemu)
else:
    print("Huruf tidak ditemukan")