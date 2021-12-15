# 2309 : 일곱난쟁이
# 100 = 9난쟁이 - 2가짜난쟁이

from itertools import combinations

dwarf_list = [int(input()) for _ in range(9)]
dwarf_7_comb = list(combinations(dwarf_list, 7))
for dwarf in dwarf_7_comb:
  if sum(dwarf) == 100:
    answer = list(dwarf)
    break
answer.sort()
for i in answer:
  print(i)