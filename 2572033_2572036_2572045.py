# Nama File
# Nama Penulis: 
# Tujuan Program: 
# Kamus Data: 
# Name_List: var. kumpulan username[str]
# Pw_List: var. kumpulan password[str]
# U_name: var input username (str)
# U_pw: var input password (str)

def initiation():
    ## Keterangan list pengguna: 
    # [0][...] : username (str)
    # [1][...] : user password (str)
    # [2][...] : user authority (str) 
    global pengguna 
    pengguna = [[None]*100 for i in range(3)]
    pengguna[0][0] = "admin1"
    pengguna[1][0] = "adml00"
    pengguna[2][0] = "administrator"
    pengguna[0][0] = "customer1"
    pengguna[1][0] = "adml00"
    pengguna[2][0] = "administrator"
    
    ## Keterangan list peralatan: 
    # [0][...] : nama peralatan (str)
    # [1][...] : kondisi (int)
    global peralatan 
    peralatan = [[None]*100 for i in range(2)]
    
    ## Keterangan list pemesanan: 
    # [0][...] : total harga (int)
    # [1][...] : berat (int)
    # [2][...] : index pelanggan (str)
    # [3][...] : hari (int)
    # [4][...] : bulan (int)
    # [5][...] : tahun (int)
    # [6][...] : jenis cucian (int)
    # [7][...] : status cucian (str)
    global pemesanan 
    pemesanan = [[None]*100 for i in range(8)]
    
    ## Keterangan list pembayaran: 
    # [0][...] : total harga (int)
    # [1][...] : dibayar (int)
    # [2][...] : index pelanggan (str)
    # [3][...] : hari (int)
    # [4][...] : bulan (int)
    # [5][...] : tahun (int)
    # [6][...] : status pembayaran (int/str)
    global pemesanan 
    pemesanan = [[None]*100 for i in range(7)]
    
    
    
    
def main():
    lanjut = 1
    initiation()
    while lanjut > 0: 
        print("Sistem Manajemen Laundry")
        print("="*30)
        U_name = int(input("Silakan Masukkan Username : "))
        U_pw = int(input("Silakan Masukkan Password : "))
        

    
    