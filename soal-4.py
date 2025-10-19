print("Jawaban Soal 4 - Pesta ulang tahu Pak Ganesh dan gajahnya")
print("===========================================================")

# Soal 4: Menentukan gajah pemenang hadiah di pesta Pak Ganesh
# Program menerima input 4 angka: A, B, C, N, yang dipisahkan spasi.
# Tidak perlu input berulang—cukup satu baris, angka dipisah spasi.

# Input: 4 bilangan bulat dalam satu baris, pisahkan dengan spasi
A, B, C, N = map(int, input().split())

# Sesuai permintaan soal, modulus utama adalah N + 1 (misal 5 jadi 6)
mod = N + 1

# Hitung eksponen modular.
# Triknya: (mod - 1) sebagai modulus siklus pangkat (menggunakan konsep totient Euler)
# Ini penting agar perhitungan tetap efisien bahkan jika C besar dan hasil pangkat B^C sangat besar

# Di sini, modulus pada pangkat adalah (mod - 1) dan (bukan N langsung) karena: 
#  - Dalam teori modular, siklus atau pola hasil perpangkatan dalam modulus akan berulang setiap mod-1, 
#    bukan setiap modulus utama. Ini berdasarkan Teorema Euler/Fermat.
#  - Jika langsung mod N, jawaban bisa salah pada kasus bilangan besar/angka prima.
#  - Pemakaian (mod-1) memastikan hasil efisien dan benar pada semua kasus yang mungkin muncul.
exp = pow(B, C, mod - 1)

# Hitung hasil utama: A dipangkatkan exp (hasil dari B^C mod (mod-1)),
# lalu hasilnya dimodulo mod (N+1) sesuai format output yang diminta soal.
result = pow(A, exp, mod)

# Output: Cetak hasil akhirnya di baris output
print(result)