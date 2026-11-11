# Proyek Loji 1 - Sistem Enkripsi 
# Nama: siapa? ytta
# NIM: YTTA

# Data status dunia
data_status_dunia = {
    "amerika": "stabil",
    "vietnam": "stabil",
    "kamboja": "goyah",
    "indonesia": "goyah",
    "iran": "goyah",
    "russia": "terganggu",
    "china": "berkembang",
    "jepang": "krisis"
}

# Fungsi khusus untuk force close / pembatalan sistem
def panggil_darurat():
    print("\n[ALERT] KODE DARURAT TERDETEKSI: 'loji pengkhianat'!")
    print("LOJI: SAYA BUKAN PENGKHIANAT!...")
    exit()
    
def panggil_darurat():
    print("\n[ALERT] KODE DARURAT TERDETEKSI: 'ytta'!")
    print("LOJI: GOBLOK -loji...")
    exit()

def jalankan_loji():
    print("=" * 55)
    print("PROYEK LOJI")
    print("=" * 55)
    print("Info: hargai loji, jangan bikin dia marah.\n")
    
    # 1. Input Data Dasar 
    nama = input("Masukkan Nama anda: ")
    if "loji pengkhianat" in nama.lower():
        panggil_darurat()
        # Cek kondisi kedua: kalau nulis "ytta"

    if "ytta" in nama.lower():
        print("LOJI: Goblok!-loji")
        panggil_darurat()

    if "helpme" in nama.lower():
        print("LOJI: hai, silakan masukkan kode negara dan sistem militer untuk akses database -loji")
            
    tujuan = input("Masukkan Tujuan: ")
    if "loji pengkhianat" in tujuan.lower():
        panggil_darurat()
    
    print("\n--- OTENTIKASI ENKRIPSI KODE ---")
    
    # 2. Input Enkripsi (Negara & Sistem Militer)
    negara_input = input("Masukkan Kode Negara (Enkripsi) : ")
    if "loji pengkhianat" in negara_input.lower():
        panggil_darurat()
        
    sistem_input = input("Masukkan Sistem Militer         : ")
    if "loji pengkhianat" in sistem_input.lower():
        panggil_darurat()
        
    # Menampilkan Laporan Awal
    print("\n" + "=" * 55)
    print("STATUS OTENTIKASI BERHASIL")
    print("=" * 55)
    print(f"Komandan        : {nama}")
    print(f"Tujuan          : {tujuan}")
    
    # 3. Validasi Keamanan Enkripsi (Syarat: Negara ZIRCON dan Sistem BASH)
    if negara_input.upper() == "ZIRCON" and sistem_input.upper() == "BASH":
        print("Status Enkripsi : DITERIMA, selamat datang ZIRCON -loji")
        print("-" * 55)
        
        # Jika lolos enkripsi, user diizinkan melihat status negara
        pilih_negara = input("Cek status database negara (cth: indonesia/china): ").strip().lower()
        if "loji pengkhianat" in pilih_negara:
            panggil_darurat()
            
        print("\n--- HASIL PEMERINTAHAN / GEOPOLITIK ---")
        if pilih_negara in data_status_dunia:
            status = data_status_dunia[pilih_negara]
            print(f"Negara Dipantau : {pilih_negara.capitalize()}")
            print(f"Status Geopolitik: {status.upper()}")
        else:
            print(f"Negara '{pilih_negara}' tidak terdaftar dalam database Loji.")
    else:
        # Jika salah, akses ditolak
        print("Status Enkripsi : GAGAL / INVALID")
        print("[AKSES DITOLAK] Enkripsi tidak valid!")
        print("Alasan : tidak terdaftar sebagai admin -loji")
        
    print("=" * 55)

# Menjalankan program utama
jalankan_loji()