# 9076 : 점수 집계

n = int(input())
score_list = [list(map(int, input().split())) for _ in range(n)]
for i in score_list:
  i.sort()
  if i[3] - i[1] > 3:
    print('KIN')
  else:
    print(i[1]+i[2]+i[3])