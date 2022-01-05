# 13301 : 타일 장식물
n = int(input())
dp = [0] * 100
dp[1] = 1

for i in range(2, n+2):
  dp[i] = dp[i-1] + dp[i-2]

answer = (dp[n] + dp[n+1])*2
print(answer)