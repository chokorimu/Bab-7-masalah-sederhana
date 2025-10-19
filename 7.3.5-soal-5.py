def hitung_lps(string_kasus):
    reversed_string = string_kasus[::-1]
    panjang_string = len(string_kasus)

    dp = [[0 for _ in range(panjang_string + 1)] for _ in range(panjang_string + 1)]
    
    for i in range(1, panjang_string + 1):
        for j in range(1, panjang_string + 1):
            if string_kasus[i-1] == reversed_string[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] 
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[panjang_string][panjang_string]

while True:
    N_input = input("Masukkan jumlah kasus (N): ")
    if not N_input.isdigit():
        print("Input tidak benar, mohon ulangi lagi.")
        continue

    N = int(N_input)
    if not (1 <= N <= 50):
        print("Jumlah kasus harus antara 1 sampai 50.")
        continue

    retval = []

    for i in range(N):
        while True:
            string_input = input(f"Masukkan string ke-{i+1}: ")
            if 1 <= len(string_input) <= 50:
                panjang = hitung_lps(string_input)
                retval.append(panjang)
                break
            else:
                print("Panjang string harus antara 1 sampai 50 karakter. Ulangi lagi!")

    print("\n--- Hasil Panjang Palindrom Terpanjang ---")
    for hasil in retval:
        print(hasil)
    break