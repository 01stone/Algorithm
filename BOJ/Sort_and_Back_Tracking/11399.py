n = int(input())
time = list(map(int, input().split()))

time.sort()
ans = 0

for i in range(n):
  for j in range(i+1):
    ans += time[j]

print(ans)