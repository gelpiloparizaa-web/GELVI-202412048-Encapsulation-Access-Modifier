class BankAccount:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            return f"Berhasil setor {jumlah}. Saldo: {self.saldo}"
        return "Jumlah setor harus positif"

    def tarik(self, jumlah):
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
            return f"Berhasil tarik {jumlah}. Saldo: {self.saldo}"
        return "Saldo tidak mencukupi"

    def info_saldo(self):
        return f"Saldo {self.pemilik}: {self.saldo}"


# Testing
akun = BankAccount("Alice", 1000)
print(akun.setor(500))
print(akun.tarik(200))
print(akun.info_saldo())
