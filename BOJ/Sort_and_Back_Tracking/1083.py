# 1083 : 소트
# 버블정렬

n = int(input())
a = list(map(int, input().split()))
s = int(input())

for i in range(n-1):
  if s == 0:
    break
  max, idx = a[i], i
  for j in range(i+1, min(n, i+1+s)):
    if max < a[j]:
      max = a[j]
      idx = j
  s -= idx - i
  for k in range(idx, i, -1):
    a[k] = a[k-1]
  a[i] = max

print(' '.join(map(str, a)))