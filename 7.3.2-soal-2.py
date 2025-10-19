import math

while True:
    jumlah_pedagang = int(input("Masukkan jumlah pedagang: "))
    if 2 <= jumlah_pedagang <= 20:
        retval = []
        for i in range(1, jumlah_pedagang):
            while True:
                kunjungan = int(input(f"Masukkan frekuensi kunjungan ke-{i}: "))
                if 1 <= kunjungan <= 100000:
                    retval.append(kunjungan)
                    break
                else:
                    print("Jumlah kunjungan harus antara 1 dan 100000.")
        print(math.lcm(*retval))
    else:
        print("Jumlah pedagang harus antara 2 dan 20.")
