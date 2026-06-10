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
def find(key,pos,data):
    find = 0
# ------------------- !
    for i in range(length(data,pos)):
        if data[i][pos] == key:
            find += 1
    if find > 0: 
        return i
    return 0

## Tujuan fungsi: Mengembalikan panjang list
## Kamus lokal:
# arr = var. list argumen(list)
# x = var. panjang arr terisi(int)
def length(arr,pos):
    x = 0
    while arr[x][pos] != None:
        x+=1
    return x


def initiation():
    ## Keterangan list pengguna: 
    # [...][0] : username (str)
    # [...][1] : user password (str)
    # [...][2] : user authority (str) 
    global pengguna 
    pengguna = [[None]*3 for i in range(200)]
    pengguna[0][0] = "admin1"
    pengguna[0][1] = "adml00"
    pengguna[0][2] = "administrator"
    pengguna[1][0] = "customer1"
    pengguna[1][1] = "cstmr--0001"
    pengguna[1][2] = "customer"
    pengguna[2][0] = "customer2"
    pengguna[2][1] = "cstmr--0002"
    pengguna[2][2] = "customer"
    pengguna[3][0] = "customer3"
    pengguna[3][1] = "cstmr--0003"
    pengguna[3][2] = "customer"
    
    ## Keterangan list peralatan: 
    # [...][0] : nama peralatan (str)
    # [...][1] : kondisi (int)
    global peralatan 
    peralatan = [[None]*2 for i in range(100)]
    
    ## Keterangan list pemesanan: 
    # [i0 | j1,j2,j3] [i1 | j1,j2,j3] [i0 | j1,j2,j3]
    # [...][0] : total harga (int) 
    # [...][1] : berat (int)
    # [...][2] : index pelanggan (str)
    # [...][3] : hari (int)
    # [...][4] : bulan (int)
    # [...][5] : tahun (int)
    # [...][6] : waktu cucian (int)
    # [...][7] : jenis laundry (int)
    # [...][8] : status cucian (str)
    global arr_pemesanan 
    arr_pemesanan = [[None]*8 for i in range(1000)]
    
    ## Keterangan list pembayaran: 
    # [...][0] : total harga (int)
    # [...][1] : dibayar (int)
    # [...][2] : index pelanggan (str)
    # [...][3] : hari (int)
    # [...][4] : bulan (int)
    # [...][5] : tahun (int)
    # [...][6] : status pembayaran (int/str)
    global arr_pembayaran 
    arr_pembayaran = [[None]*7 for i in range(1000)]
    
def login():
    U_name = str(input("Silakan Masukkan Username : "))
    U_pw = str(input("Silakan Masukkan Password : "))
    idx = 0
    while pengguna[idx][0] != None :
        if pengguna[idx][0] == U_name:
            if pengguna[idx][1]    
        if pengguna[idx][2] == "administrator":
            return 1
        elif pengguna[idx][2] == "customer":
            return 2
        idx += 1 
    print("Pengguna tidak ditemukan")
    print("Menginisiasi user baru...\n")
    pengguna[idx][0] = input(("Masukkan ulang username : "))
    pengguna[idx][1] = input(("Masukkan password : "))
    pengguna[idx][2] = "customer"
    print("Selamat datang,",pengguna[idx][1])
    return 2

def pemesanan(C):
    # arr_pemesanan[C][0]= int(input("ID Struk"))
    arr_pemesanan[C][1]= str(input("Berat cucian: "))
    # arr_pemesanan[C][2]= str(input("Tanggal Pemesanan"))
    
    # Jenis - Waktu - Aksi(++)
    # JC = Jenis Cucian
    # PP = Pilihan Paket
    print("\nJenis Pakaian:\nPakaian(1)\nSelimut(2)\nSprei(3)\nSepatu(4)\nTas(5)\n}","-"*20)
    JC = int(input("Masukkan jenis cucian: "))
    if (JC==1):
        print ("\nMasukkan jenis cucian\n","-"*20)
        print ("[1] Cuci Pakaian 6 jam - Rp. 14.000/kg")
        print ("[2] Cuci Pakaian 12 jam - Rp. 12.000/kg")
        print ("[3] Cuci Pakaian 24 jam - Rp. 10.000/kg")
        print ("[4] Cuci Pakaian 2-3 hari - Rp. 8.000/kg")
    elif (JC==2):
        print ("[5] Cuci Selimut 1 hari - Rp. 20.000/pc")
        print ("[6] Cuci Selimut 2-3 hari - Rp. 15.000/pc")
    elif (JC==3):
        print ("[7] Cuci Sprei 1 hari - Rp. 20.000/set")
        print ("[8] Cuci Sprei 2-3 hari - Rp. 15.000/set")
    elif (JC==4):
        print ("[9] Cuci Sepatu 1 hari - Rp. 30.000/pair")
        print ("[10] Cuci Sepatu 2-3 hari - Rp. 22.000/pair")
    elif (JC==5):
        print ("[11] Cuci Tas 1 hari - Rp 40.000/pc")
        print ("[12] Cuci Tas 2-3 hari - Rp 30.000/pc")
    PP = int(input("Masukkan paket pesanan: ")) 
        
    arr_pemesanan[C][7]= PP
    
    # Pakaian
    if (JC == 1):
        if (PP==1):        
            arr_pemesanan[C][5] = 14000*arr_pemesanan[C][1]
        elif (PP==2):
            arr_pemesanan[C][5] = 12000*arr_pemesanan[C][1]
        elif (PP==3):
            arr_pemesanan[C][5] = 10000*arr_pemesanan[C][1]
        elif (PP==4):
            arr_pemesanan[C][5] = 8000*arr_pemesanan[C][1]
        # Selimut
    elif (JC == 2):
        if (PP==5):
            arr_pemesanan[C][5] = 20000*arr_pemesanan[C][1]
        elif (PP==6):
            arr_pemesanan[C][5] = 15000*arr_pemesanan[C][1]
    # Sprei
    elif (JC == 3):
        if (PP==7):
            arr_pemesanan[C][5] = 20000*arr_pemesanan[C][1]
        elif (PP==8):
            arr_pemesanan[C][5] = 15000*arr_pemesanan[C][1]
    # Sepatu
    elif (JC == 4):
        if (PP==9):
            arr_pemesanan[C][5] = 30000*arr_pemesanan[C][1]
        elif (PP==10):
            arr_pemesanan[C][5] = 22000*arr_pemesanan[C][1]
    # Tas
    elif (JC == 5):
        if (PP==11):
            arr_pemesanan[C][5] = 40000*arr_pemesanan[C][1]
        elif (PP==12):
            arr_pemesanan[C][5] = 30000*arr_pemesanan[C][1]
    else:
        print ("Pilihan invalid")
        pemesanan()
# Status Cucian (queue/WAIT)     
    # arr_pemesanan[C][6]= str(input("Status Cucian(Y/N)"))
    
    C = C + 1
    return 0

def main():
    global id
    global C
    C = 0 
    lanjut = 1
    initiation()
    while lanjut > 0: 
        print("Sistem Manajemen Laundry")
        print("="*30)
        auth = login()
        # print("Selamat datang,", pengguna[0][id])
        print("-"*30)
        print("Silakan masukkan aksi")
        if auth == 1:
            print("[1] Menambahkan akun admin")
            print("[2] Mengecek kondisi peralatan")
            print("[3] Mengecek riwayat pemesanan")
            print("[4] Mengecek list pembayaran")
            print("[5] Statistik")
            print("[6] Keluar")
            print("-"*20)
            act = int(input("Pilihan Anda: "))
            if act == 1:
                pass
            elif act == 2:
                pass
            elif act == 3:
                pass
            elif act == 4:
                pass
            elif act == 5:
                pass
            elif act == 6:
                confirm = str(input("Apakah anda ingin log out dari akun? (Y/N): "))
                if confirm == "Y" :
                    lanjut = 0
                    login()
                else:
                    pass
        elif auth == 2:
            print("[1] Menambah pesanan")
            print("[2] Mengecek status pesanan")
            print("[3] Keluar")
            print("-"*20)
            act = int(input("Pilihan Anda: "))
            if act == 1:
                pemesanan(C)
            elif act == 2:
                pass
            elif act == 3:
                confirm = str(input("Apakah anda ingin log out dari akun? (Y/N): "))
                if confirm == "Y" :
                    lanjut = 0
                    login()
                else:
                    pass
                
            
    return 0
if __name__ == '__main__':
    main()
    
    