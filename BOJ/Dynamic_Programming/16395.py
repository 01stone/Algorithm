# 16395 : 파스칼의 삼각형

'''
# 런타임 에러
n, k = map(int, input().split())
dp = [[1 for _ in range(i)] for i in range(1, 30)]

for j in range(2, 30):
  for k in range(1, j):
    dp[j][k] = dp[j-1][k-1] + dp[j-1][k]

print(dp[n-1][k-1])
'''

n, k = map(int, input().split())
dp = [[1], [1,1]]

for i in range(2, n):
  pascal = [1]
  for j in range(1, i):
    pascal.append(dp[i-1][j-1] + dp[i-1][j])
  pascal.append(1)
  dp.append(pascal)

print(dp[n-1][k-1])