# 1015

n = int(input())
p_list = list(map(int, input().split()))
p_sorted = sorted(p_list)

i_list = []
for i in range(n):
  idx = p_sorted.index(p_list[i])
  i_list.append(idx)
  p_sorted[idx] = -1
  
print(*i_list)