class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

if __name__ == "__main__":
    # Buat 2 mata kuliah
    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Algoritma")

    # Buat 3 mahasiswa
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Andi")

    # Daftarkan mahasiswa ke masing-masing mata kuliah
    mk1.tambah_mahasiswa(m1)
    mk1.tambah_mahasiswa(m2)

    mk2.tambah_mahasiswa(m2)
    mk2.tambah_mahasiswa(m3)

    # Tampilkan daftar mahasiswa dan jumlahnya
    print(f"Daftar mahasiswa untuk {mk1.kode} - {mk1.nama}: {mk1.daftar_mahasiswa()}")
    print(f"Jumlah mahasiswa di {mk1.kode}: {mk1.jumlah_mahasiswa()}\n")

    print(f"Daftar mahasiswa untuk {mk2.kode} - {mk2.nama}: {mk2.daftar_mahasiswa()}")
    print(f"Jumlah mahasiswa di {mk2.kode}: {mk2.jumlah_mahasiswa()}\n")