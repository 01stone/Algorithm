def solution(n):
    sqrt_n = pow(n, 0.5)
    return pow(int(sqrt_n)+1, 2) if sqrt_n == int(sqrt_n) else -1