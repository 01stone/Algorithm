# 11047 : 동전 0
n, k = map(int, input().split())
n_list = [int(input()) for _ in range(n)]

cnt = 0
for i in reversed(range(n)):
  cnt += k//n_list[i]
  # print(cnt) # 50000 > 10000 > 5000 >>>> 1000(으로 4번 나누고 200 남음)
  k = k%n_list[i]
  # print(k)
print(cnt)


# 1931 : 회의실 배정
n = int(input())
shedule = [list(map(int, input().split())) for _ in range(n)]
shedule.sort(key = lambda x: (x[0], x[1]))

cnt = 1
end = shedule[0][1]
for i in range(1, n):
  if shedule[i][0] >= end:
    print(shedule[i][0])
    cnt += 1
    end = shedule[i][1]

# print(cnt)



# 11399 : ATM
'''
# 메모리 초과
from itertools import combinations, permutations

n = int(input())
time = list(map(int, input().split()))

time_p = list(permutations(time, n))

p = []
for i in time_p:
  p.append(list(i))

ans = []
for i in p:
  sum_p = []
  for j in range(n):
    sum_p.append(i[j]*(j+1))
  ans.append(sum(sum_p))

print(min(ans))
'''
n = int(input())
time = list(map(int, input().split()))

time.sort()
ans = 0

for i in range(n):
  print('i', i)
  for j in range(i+1):
    # print(time[j])
    ans += time[j]

print(ans)


# 1541 : 잃어버린 괄호
eq = input().split('-')
answer = []
for i in eq:
  # print('i', i)
  cnt = 0
  f = i.split('+')
  for j in f:
    # print(j)
    cnt += int(j)
  answer.append(cnt)
# print(answer)

num = answer[0]
for i in range(1, len(answer)):
  # print(answer[i])
  num -= answer[i]
print(num)


# 13305 : 주유소

n = int(input())
road_list = list(map(int, input().split()))
city_list = list(map(int, input().split()))

min_oil = city_list[0]
answer = 0

for i in range(n-1):
  if min_oil > city_list[i]:
    min_oil = city_list[i]
  answer += (min_oil * road_list[i])

print(answer)