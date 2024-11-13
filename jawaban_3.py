jumlahbarang = int(input('Masukan Jumlah Barang :'))
storeBarang = 0
for i in range ( 1, jumlahbarang + 1):
    hargabarang = int(input('masuakn harga barang :'))
    storeBarang += hargabarang
    total = storeBarang + hargabarang

print(f'Total Belanja : RP.{total}')
