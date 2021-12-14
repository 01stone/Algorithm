# 2750, 2751
n = int(input())
n_list = [int(input()) for i in range(n)]
n_list.sort()
for i in n_list:
    print(i)


# 10989
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)


# 2108
import sys
from collections import Counter
n = int(sys.stdin.readline())
n_list = []
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))
 
# 산술평균 - 다 더해서 / n
print(round(sum(n_list)/n))
 
# 중앙값 - 오름차순 -> 중간값
n_list.sort()
print(n_list[n//2])
 
# 최빈값 - 빈출
cnt_li = Counter(n_list).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
 
# 범위 - 최댓값-최솟값
print(max(n_list)-min(n_list))


# 1427
n = input()
n = [int(i) for i in n]

n_sort = sorted(n, reverse=True)

for j in n_sort:
    print(j, end='')


# 11650
n = int(input())

coor = []
for i in range(n):
  [a, b] = map(int, input().split())
  coor.append([a, b])

coor_sort = sorted(coor)
for j in range(n):
  print(coor_sort[j][0], coor_sort[j][1])


# 11651
n = int(input())

coor = []
for i in range(n):
  [a, b] = map(int, input().split())
  coor.append([b, a])

coor_sort = sorted(coor)
for j in range(n):
  print(coor_sort[j][1], coor_sort[j][0])


# 1181
n = int(input())
words = [str(input()) for i in range(n)]
words = list(set(words))

# lambda : 익명함수
# lambda 인자(words의 인자) : 표현식((글자수, 글자)) 
# key = 정렬을 목적으로 하는 함수를 값으로 넣음
words.sort(key = lambda x : (len(x), x))

print('\n'.join(words))


# 10814
n = int(input())
m = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    m.append((age, name))

m.sort(key = lambda x : (x[0]))

for j in m:
    print(j[0], j[1])


# 18870
n = int(input())
n_list = list(map(int, input().split()))

n_sort = sorted(list(set(n_list)))

n_dic = {n_sort[i]:i for i in range(len(n_sort))} 
for i in n_list: 
  print(n_dic[i],end=' ')