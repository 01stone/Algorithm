# 15312 : 이름 궁합

alpha_cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]
alpha_dic = dict(zip(alpha, alpha_cnt))
# print(alpha_dic)

A = list(str(input().upper()))
B = list(str(input().upper()))
n = len(A) * 2
dp  = []

for i in range(n):
  if i % 2 == 0:
    dp.append(alpha_dic[A[i//2]])
  else:
    dp.append(alpha_dic[B[i//2]])

while len(dp) > 2:
    for i in range(0, len(dp)-1):
        dp[i] = (dp[i] + dp[i+1]) % 10
    dp.pop()

# print(dp)
print(''.join(map(str, dp)))