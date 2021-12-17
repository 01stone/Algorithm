# 1026

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a = sorted(a, reverse=True)
sorted_b = sorted(b)

sum = 0
for i in range(n):
  sum += sorted_a[i] * sorted_b[i]

print(sum)