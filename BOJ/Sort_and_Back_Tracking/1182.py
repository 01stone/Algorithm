from itertools import permutations, combinations

n, s = map(int, input().split())
# print(n)
# print(s)
n_array = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
  # print('combi : ',list(combinations(n_array, i)))
  combi = combinations(n_array, i)
  for j in list(combi):
    # print(sum(j))
    if sum(j) == s:
      cnt += 1
print(cnt)