def solution(n, m):
    def gcd(a, b):
        return gcd(b, a%b) if b > 0 else a
    return [gcd(n, m), n*m//gcd(n,m)]