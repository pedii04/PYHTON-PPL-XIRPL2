# ada 3 kategori enkaspul yaitu : public, protectac, privat

class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas 
        self.tinggi = tinggi
        self luas = 0.5 * alas * tinggi

#buat instantasinya
# segitiga_besar = segitiga(100,00)

# print(f'alas : (segitiga_besar.alas)')
# print(f'tinggi : (segitiga_besar.tinggi)')
# print(f'luas : (segitiga_besar.luas)')

# contoh class protected
class mobil:
    def __init__(self, merk):
        self._merk = merk

class mobilfwan(mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)
        self._total_gear = total_gear

# Akses _merk dari subclass (kelas turunan)
def pamer(self):
    print(f'mobil(self._merk) dengan total gear (self._total_gear)')

Redbul = mobil('Redbul Racing',8)
