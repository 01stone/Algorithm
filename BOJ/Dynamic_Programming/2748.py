# 2748 : 피보나치 수2
n = int(input())
dp = [0] * 100
dp[1] = 1

for i in range(2, n+1):
  dp[i] = dp[i-2] + dp[i-1]

print(max(dp))