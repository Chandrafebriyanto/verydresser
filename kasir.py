total = 0
barang = []
harga = []

konfirmasi = True
while konfirmasi:
    print(""" Daftar Barang\n
        1. Roti \t 5000
        2. Es Cream \t 5000
        3. Buku \t 3000
        4. Pensil \t 2500
        5. Penghapus \t 1500
        """)
    
    kode = int(input("masukkan kade barang: "))
    if kode == 1:
        barang.append('roti')
        harga.append(5000)
        total += 5000
        
    elif kode == 2:
        barang.append('es cream')
        harga.append(5000)
        total += 5000
    
    elif  kode == 3:
        barang.append('buku')
        harga.append(3000)
        total += 3000
        
    elif kode == 4:
        barang.append('pensil')
        harga.append(2500)
        total += 2500
        
    elif kode == 5:
        barang.append('penghapus')
        harga.append(1500)
        total += 1500
        
    else:
        print('barang tidak ada')
        
    ipt = input("Lanjut belanja? (Y/T) ")
    if ipt == 'Y':
        konfirmasi = True
    elif ipt == 'T':
        konfirmasi = False
    else:
        print("")
    
print('barang yang dibeli: ', barang)
print('harga barang: ', harga)
print('total yang harus dibayar:', total)
    
uang = int(input("masukan uang pembayaran: "))
if uang > total:
    print("kembalian: ", uang - total)
elif uang == total:
    print("tidak ada kembalian")
else:
    print("uangnya kurang", abs(uang - total))
