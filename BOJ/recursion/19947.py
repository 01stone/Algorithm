# 19947 : 투자의 귀재 배주형

h, y = map(int, input().split())
dp = [0] * 20
dp[0] = h

for i in range(1, y+1):
    if i >= 5:
        dp[i] = int(max(dp[i-5]*1.35, dp[i-3]*1.2, dp[i-1]*1.05))
    elif i >= 3:
        dp[i] = int(max(dp[i-3]*1.2, dp[i-1]*1.05))
    else:
        dp[i] = int(dp[i-1]*1.05)  # int 처리 안하면 소수점 이상함
    

# print(dp)
print(max(dp))