# kelas induk = Kendaraan , kelas turunan = Mobil
# Kendaraan mempunyai sifat berjalan(), Mobil mempunyai sifat berjalan() tapi lebih spesifik

class kendaraan:
    def berjalan(self):
        print('berjalan')

class mobil(kendaraan):
    def berjalan(self, kecepatan, satuan = 'km/j'):
        print('berjalan lebih ngebut {kecepatan} {satuan}')

#instansiasi (mamnggil funsi dan kelas)
sepeda = kendaraan()
sedan = mobil()

sepeda.berjalan()
sedan.berjalan()