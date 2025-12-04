# File: relasi.py
# relasi aggregation

class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = [] # agregasi: Nilai dapat berdiri sendiri

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    # f. Tambahkan method rata_rata() pada class Mahasiswa
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0.0
        # Hitung rata-rata dari semua nilai yang dimiliki mahasiswa
        total_skor = sum(n.skor for n in self.daftar_nilai)
        return total_skor / len(self.daftar_nilai)

class Matakuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama

class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = [] # agregasi

    def tambah_matakuliah(self, mk: Matakuliah):
        self.daftar_matakuliah.append(mk)
        
    # d. Tampilkan daftar mata kuliah dari setiap Program Studi
    def tampilkan_matakuliah(self):
        mk_list = [f"{mk.kode} - {mk.nama}" for mk in self.daftar_matakuliah]
        print(f"Daftar Matakuliah di {self.nama}:")
        print("  " + "\n  ".join(mk_list))

# relasi composition
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi

# Fungsi report_program (seperti pada contoh latihan)
def report_program(prodi: ProgramStudi, semua_mahasiswa: list['Mahasiswa']):
    print("-" * 50)
    print(f"Laporan Program Studi: {prodi.nama}")
    print("-" * 50)
    
    # Tampilkan daftar mata kuliah
    print("Matakuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-")
    
    print("\nMahasiswa dan rata-rata nilai mata kuliah yang relevan:")
    for m in semua_mahasiswa:
        # Filter nilai yang relevan dengan mata kuliah di prodi ini
        prodi_mk_kodes = [mk.kode for mk in prodi.daftar_matakuliah]
        relevan = [n for n in m.daftar_nilai if n.kode_mk in prodi_mk_kodes]
        
        # Hitung rata-rata hanya untuk mata kuliah di prodi ini
        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f"-> {m.nim} - {m.nama}: Rata-rata Nilai Relevan = {round(avg, 2)}")
        else:
            print(f"-> {m.nim} - {m.nama}: (Tidak ada nilai relevan dengan prodi ini)")
    
    print("-" * 50)


if __name__ == "__main__":
    uni = Universitas("Universitas ABC")
    
    # Program Studi yang sudah ada
    prodi_ti = uni.buat_program("Teknik Informatika")
    
    # a. Tambahkan 2 Program Studi baru
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_ak = uni.buat_program("Akuntansi")
    
    # b. Tambahkan minimal 2 Mata Kuliah untuk masing-masing Program Studi
    mk_ti1 = Matakuliah("TI101", "Pemrograman Dasar")
    mk_ti2 = Matakuliah("TI102", "Struktur Data")
    prodi_ti.tambah_matakuliah(mk_ti1)
    prodi_ti.tambah_matakuliah(mk_ti2)

    mk_si1 = Matakuliah("SI101", "Basis Data")
    mk_si2 = Matakuliah("SI102", "Jaringan Komputer")
    prodi_si.tambah_matakuliah(mk_si1)
    prodi_si.tambah_matakuliah(mk_si2)

    mk_ak1 = Matakuliah("AK101", "Pengantar Akuntansi")
    mk_ak2 = Matakuliah("AK102", "Audit")
    prodi_ak.tambah_matakuliah(mk_ak1)
    prodi_ak.tambah_matakuliah(mk_ak2)

    # c. Buat 3 Mahasiswa
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Ahmad")
    semua_mahasiswa = [m1, m2, m3]

    # c. Tambahkan beberapa objek Nilai ke mahasiswa
    # Nilai M1 (Budi) - fokus ke TI dan SI
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("SI101", 92))
    m1.tambah_nilai(Nilai("TI102", 78))
    m1.tambah_nilai(Nilai("AK101", 60)) # Nilai dari prodi lain

    # Nilai M2 (Siti) - fokus ke SI dan AK
    m2.tambah_nilai(Nilai("SI101", 90))
    m2.tambah_nilai(Nilai("AK102", 88))
    m2.tambah_nilai(Nilai("SI102", 75))
    
    # Nilai M3 (Ahmad) - fokus ke TI
    m3.tambah_nilai(Nilai("TI101", 80))
    m3.tambah_nilai(Nilai("TI102", 70))


    print("="*60)
    print(f"PROGRAM LATIHAN RELASI CLASS: {uni.nama}")
    print("="*60)

    # d. Tampilkan daftar mata kuliah dari setiap Program Studi
    print("\n--- DAFTAR MATA KULIAH SETIAP PROGRAM STUDI ---")
    prodi_ti.tampilkan_matakuliah()
    prodi_si.tampilkan_matakuliah()
    prodi_ak.tampilkan_matakuliah()
    print("-" * 50)


    # e. Tampilkan daftar nilai untuk setiap mahasiswa
    print("\n--- DAFTAR NILAI DAN RATA-RATA SEMUA MAHASISWA ---")
    for m in semua_mahasiswa:
        nilai_str = ", ".join([f"{n.kode_mk}: {n.skor}" for n in m.daftar_nilai])
        # f. Tampilkan rata-rata nilai setiap mahasiswa (rata-rata semua matkul)
        print(f"*{m.nim} - {m.nama}: Nilai = [{nilai_str}] | Rata-rata SEMUA Nilai = {round(m.rata_rata(), 2)}")
    print("-" * 50)


    # g. Panggil fungsi report_program untuk setiap Program Studi.
    print("\n--- LAPORAN NILAI BERDASARKAN PROGRAM STUDI ---")
    report_program(prodi_ti, semua_mahasiswa)
    report_program(prodi_si, semua_mahasiswa)
    report_program(prodi_ak, semua_mahasiswa)