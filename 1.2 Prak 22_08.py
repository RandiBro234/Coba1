banyak = int(input('Masukan banyak angka: '))
kosong = []
def kali():
    for bilangan in range(banyak):
        angka = int(input("Masukkan angka: "))
        hasil_kali = angka*3
        kosong.append(hasil_kali)
kali()
print(kosong)
print("aku ganteng")
