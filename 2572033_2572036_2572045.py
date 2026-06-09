# Nama File: Sistem Informasi Laundry
# Nama Penulis: Joseph Xavier Tan - 2572033
#               Timothy Suharli - 2572036
#               Yosia Krisanusama - 2572045
# Tujuan Program: 
# Kamus Data: 
# Name_List: var. kumpulan username[str]
# Pw_List: var. kumpulan password[str]
# U_name: var input username (str)
# U_pw: var input password (str)


## Tujuan fungsi: Mereturn apakah yang dicari ada di fungsi
## Kamus lokal: 
# i = var. pengendali loop(int)
# key = var. argumen nilai dicari(int) 
# key = var. argumen array(list) 
def find(key,data):
    find = 0
    for i in range(length(data)):
        if data[i] == key:
            find += 1
    if find > 0: 
        return i
    return 0

## Tujuan fungsi: Mengembalikan panjang list
## Kamus lokal:
# arr = var. list argumen(list)
# x = var. panjang arr terisi(int)
def length(arr):
    x = 0
    while arr[x][0] != None:
        x+=1
    return x


def initiation():
    ## Keterangan list pengguna: 
    # [0][...] : username (str)
    # [1][...] : user password (str)
    # [2][...] : user authority (str) 
    global pengguna 
    pengguna = [[None]*200 for i in range(3)]
    pengguna[0][0] = "admin1"
    pengguna[1][0] = "adml00"
    pengguna[2][0] = "administrator"
    pengguna[0][0] = "customer1"
    pengguna[1][0] = "cstmr--0001"
    pengguna[2][0] = "customer"
    pengguna[0][0] = "customer2"
    pengguna[1][0] = "cstmr--0002"
    pengguna[2][0] = "customer"
    pengguna[0][0] = "customer3"
    pengguna[1][0] = "cstmr--0003"
    pengguna[2][0] = "customer"
    
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
    pemesanan = [[None]*1000 for i in range(8)]
    
    ## Keterangan list pembayaran: 
    # [0][...] : total harga (int)
    # [1][...] : dibayar (int)
    # [2][...] : index pelanggan (str)
    # [3][...] : hari (int)
    # [4][...] : bulan (int)
    # [5][...] : tahun (int)
    # [6][...] : status pembayaran (int/str)
    global pemesanan 
    pemesanan = [[None]*1000 for i in range(7)]
    
def login():
    U_name = int(input("Silakan Masukkan Username : "))
    U_pw = int(input("Silakan Masukkan Password : "))
    for i in range(length(pengguna)):
        if find(U_name,pengguna[0]) == 1:
            if pengguna[2][i] == "administrator":
                return 1
            elif pengguna[2][i] == "customer":
                return 2
    return 0

def main():
    lanjut = 1
    initiation()
    while lanjut > 0: 
        print("Sistem Manajemen Laundry")
        print("="*30)
        is_found = find(U_name,pengguna[0])
        if is_found == 0:
            
        
if __name__ == '__main__':
    main()
    
    