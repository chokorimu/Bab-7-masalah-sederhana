A, B, C, N = map(int, input("Input A, B, C, dan N; dipisahkan dengan spasi:\n").split())
mod = N + 1
exp = pow(B, C, mod - 1)
result = pow(A, exp, mod)
print(result)
