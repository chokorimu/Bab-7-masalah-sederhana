print("programm mencari median perusahaan")
#input() yang akan membaca baris pertama
N=int(input())
#buat lis kosong untuk menampung semua nilai
daftar_nilai=[]
#loop sebanyak N kali untuk membaca nilai
for _ in range(N) :
    #Baca nilai di tiap baris dan ubah jadi angka
    nilai=int(input())
    #Masukan angka dalam list
    daftar_nilai.append(nilai)
    #urutkan daftar nilai dari yang terkecil sampai yang terbesar
    daftar_nilai.sort()
if N %2==1 :
    #kasus ganjil
    index_tengah = N//2
    median = daftar_nilai[index_tengah]
else :
    #kasus genap
    index_kiri = N//2
    index_kanan = index_kiri + 1
    median = (daftar_nilai[index_kiri] + daftar_nilai[index_kanan])/2
#Cetak hasil dengan format .1f (satu angka di belakang koma)
print(f"{median:.1f}")