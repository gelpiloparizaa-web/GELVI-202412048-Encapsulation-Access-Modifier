# Tugas Praktikum D: Sistem OOP Perpustakaan Sederhana
# Implementasi Encapsulation dan Relasi Antar Class

class Buku:
    def __init__(self, judul, penulis, kode, stok, lokasi):
        self.judul = judul        
        self.penulis = penulis    
        self.kode_buku = kode     
        self._stok = stok         
        self.__lokasi_rak = lokasi

    def get_lokasi_rak(self): return self.__lokasi_rak
    def set_lokasi_rak(self, baru): self.__lokasi_rak = baru
    
    def tambah_stok(self, j): self._stok += j
    def kurangi_stok(self, j):
        if self._stok < j: raise ValueError("Stok tidak cukup.")
        self._stok -= j
        return True
    
    def info_buku(self): 
        # Output disesuaikan agar sama persis dengan yang diminta
        return f"[{self.kode_buku}] {self.judul} ({self.penulis}) | Stok: {self._stok}, Rak: {self.__lokasi_rak}"

class Peminjaman: 
    def __init__(self, buku: Buku, anggota: 'Anggota', tgl_pinjam):
        self.buku_dipinjam = buku     
        self.anggota_peminjam = anggota 
        self.tanggal_pinjam = tgl_pinjam
        self.tanggal_kembali = None
        self.status = 'Dipinjam'

    def kembalikan(self, tgl_kembali):
        self.tanggal_kembali = tgl_kembali
        self.status = 'Dikembalikan'
        
    def info_peminjaman(self): 
        status_info = f"Pinjam: {self.tanggal_pinjam}"
        if self.status == 'Dikembalikan': status_info += f", Kembali: {self.tanggal_kembali}"
        return f"- '{self.buku_dipinjam.judul}' | Status: {self.status} ({status_info})"

class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam=2):
        self.id_anggota = id_anggota  
        self.nama = nama              
        self._maks_pinjam = maks_pinjam 
        self.__status_aktif = True    
        self.daftar_peminjaman = [] 

    def get_status_aktif(self): return "Aktif" if self.__status_aktif else "Nonaktif"
    def set_status_aktif(self, status): self.__status_aktif = status
        
    def get_pinjam_aktif(self):
        return sum(1 for p in self.daftar_peminjaman if p.status == 'Dipinjam')

    def pinjam_buku(self, buku, tgl_pinjam): 
        if self.get_pinjam_aktif() >= self._maks_pinjam:
            print(f"[!] Gagal pinjam: {self.nama} telah mencapai batas pinjam ({self._maks_pinjam}).")
            return None
        try:
            # Perhatikan: stok sisa dicetak dari atribut _stok
            buku.kurangi_stok(1)
            pinjam = Peminjaman(buku, self, tgl_pinjam)
            self.daftar_peminjaman.append(pinjam)
            print(f"[+] Sukses pinjam: {self.nama} - '{buku.judul}'. Stok sisa: {buku._stok}")
            return pinjam
        except ValueError as e:
            print(f"[!] Gagal pinjam: {e}")
            return None

    def kembalikan_buku(self, peminjaman, tgl_kembali): 
        if peminjaman.status == 'Dipinjam':
            peminjaman.kembalikan(tgl_kembali)
            peminjaman.buku_dipinjam.tambah_stok(1)
            print(f"[+] Sukses kembali: {self.nama} - '{peminjaman.buku_dipinjam.judul}'.")
            return True
        return False

    def info_anggota(self): 
        return (f"ID: {self.id_anggota}, Nama: {self.nama}, Status: {self.get_status_aktif()}, "
                f"Pinjam Aktif: {self.get_pinjam_aktif()}/{self._maks_pinjam}")

class Perpustakaan: 
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = [] 
        self.daftar_anggota = []

    def tambah_buku(self, *args):
        buku_baru = Buku(*args)
        self.daftar_buku.append(buku_baru)
        print(f"Buku '{buku_baru.judul}' ditambahkan.")
        return buku_baru

    def tambah_anggota(self, id_anggota, nama):
        anggota_baru = Anggota(id_anggota, nama)
        self.daftar_anggota.append(anggota_baru)
        print(f"Anggota '{anggota_baru.nama}' didaftarkan.")
        return anggota_baru

# --- DEMONSTRASI (Menghasilkan output yang diminta) ---
if __name__ == "__main__":
    
    perpus = Perpustakaan("Perpus STITEK")
    print("="*60)
    print("DEMONSTRASI TUGAS PRAKTIKUM D: SISTEM PERPUSTAKAAN")
    print("="*60)
    
    # Inisialisasi: menggunakan nilai yang menghasilkan output yang diminta
    b1 = perpus.tambah_buku("Python OOP", "Ahmad", "P001", 2, "A-101")
    b2 = perpus.tambah_buku("Struktur Data", "Budi", "SD02", 1, "A-102")
    b3 = perpus.tambah_buku("Dasar Jaringan", "Candra", "JK03", 5, "B-201")
    print("\n")

    a1 = perpus.tambah_anggota("M001", "Ani")
    a2 = perpus.tambah_anggota("M002", "Bima")
    print("-" * 60)
    
    # 1. INFORMASI BUKU AWAL:
    print("1. INFORMASI BUKU AWAL:")
    print(b1.info_buku()); print(b2.info_buku()); print(b3.info_buku())
    print("-" * 60)
    
    # 2. PROSES PINJAM:
    print("2. PROSES PINJAM:")
    p1 = a1.pinjam_buku(b1, "2025-12-01") 
    p2 = a1.pinjam_buku(b2, "2025-12-01") 
    a1.pinjam_buku(b3, "2025-12-03") # Gagal
    p3 = a2.pinjam_buku(b3, "2025-12-02")
    print("-" * 60)
    
    # 3. LAPORAN PINJAMAN AKTIF:
    print("3. LAPORAN PINJAMAN AKTIF:")
    print(a1.info_anggota())
    for p in a1.daftar_peminjaman: 
        # Hanya tampilkan yang masih 'Dipinjam'
        if p.status == 'Dipinjam': print(p.info_peminjaman())
    
    print(a2.info_anggota())
    for p in a2.daftar_peminjaman: 
        if p.status == 'Dipinjam': print(p.info_peminjaman())
    print("-" * 60)
    
    # 4. PROSES PENGEMBALIAN:
    print("4. PROSES PENGEMBALIAN:")
    if p1: a1.kembalikan_buku(p1, "2025-12-04")
    
    # HASIL AKHIR
    print("\n--- HASIL AKHIR ---")
    print(f"Buku P001 setelah dikembalikan: {b1.info_buku()}")
    print(f"Ani setelah mengembalikan: {a1.info_anggota()}")
    print("-" * 60)