class Buku:
    # Class attribute
    perpustakaan = "Perpustakaan STITEK"

    # Constructor
    def __init__(self, judul, penulis, tahun):
        # Instance attributes
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info_buku(self):
        return f"Buku {self.judul} oleh {self.penulis} ({self.tahun})"


# Instansiasi object
buku1 = Buku("Sistem Operasi", "Lapu Tombi Layuk", 2025)
buku2 = Buku("Pemograman Berorientasi", "Abadi Nugroho", 2025)

print(buku1.info_buku())
print(buku2.info_buku())
print(f"Lokasi: {Buku.perpustakaan}")
