N = int(input())

for i in range(N):
    baris = input().split()
    T = int(baris[0])
    skor = []

    for _ in range(1, len(baris)):
        skor.append(int(baris[_]))

    total_max = 3 * T * (T-1) // 2
    total_skor = sum(skor)
    
    if total_skor <= total_max:
        print("YESSSSSS")
    else:
        print("NOOOOOOOOOO")