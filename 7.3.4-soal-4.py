while True:
    A, B, C, N = map(int, input("Input A, B, C, dan N; dipisahkan dengan spasi:\n").split())
    if 0 <= A <= 1*10**3 and 0 <= B <= 2*10**4 and 0 <= C <= 3*10**5 and 1 <= N <= 10**7:
        break
    print("Input tidak valid, silakan coba lagi.")

mod = N + 1
exp = pow(B, C, mod - 1)
result = pow(A, exp, mod)
print(result)
