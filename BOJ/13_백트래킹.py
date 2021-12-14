# 15649
n, m = map(int, input().split())
visited = [False]*n
result = []

def back_tracking(depth, n, m):
  if depth == m:
    # print(result)
    print(' '.join(map(str, result)))
    return
  for i in range(len(visited)):
    if not visited[i]:
      visited[i] = True
      result.append(i+1)
      back_tracking(depth+1, n, m)
      visited[i] = False
      result.pop()

back_tracking(0, n, m)


# 15650
from itertools import combinations

n, m = map(int, input().split())
c = combinations(range(1, n+1), m)
for i in c:
  print(' '.join(map(str, i)))


# 15651
n, m = map(int, input().split())
visited = [False]*n
result = []

def back_tracking(depth, n, m):
  if depth == m:
    # print(result)
    print(' '.join(map(str, result)))
    return
  for i in range(len(visited)):
    if not visited[i]:
      # visited[i] = True
      result.append(i+1)
      back_tracking(depth+1, n, m)
      # visited[i] = False
      result.pop()

back_tracking(0, n, m)


# 15652
n, m = map(int, input().split())
# visited = [False]*n
result = []

def back_tracking(depth, idx, n, m):
  if depth == m:
    print(' '.join(map(str, result)))
    return
  for i in range(idx, n):
    result.append(i+1)
    back_tracking(depth+1, i, n, m)
    result.pop()

back_tracking(0, 0, n, m)


# 9663
# answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
# n = int(input())
# print(answer[n])
def check(x):
  for i in range(x):
    if col[x] == col[i] or abs(col[i]-col[x]) == (x-i):
      return False
  return True

def bt(x):
  global result
  if x == n:
    result += 1
  else:
    for i in range(n):
      col[x] = i
      if check(x):
        bt(x+1)

n = int(input())
col = [0] * n
result = 0
bt(0)
print(result)


# 14888
from itertools import permutations #순열 함수

n = int(input())
n_list = list(map(int, input().split()))
plus, minus, multiple, division = map(int, input().split())

operation_list = []
operation_list += ['+'] * plus
operation_list += ['-'] * minus
operation_list += ['*'] * multiple
operation_list += ['%'] * division
# print(operation_list)

operation_set = []
for numbers in list(permutations(operation_list)):
    operation_set.append(numbers)
operation_set = list(set(operation_set))
# print(operation_set)

max = -1000000001
min = 1000000001
for case in operation_set:
    answer = n_list[0]
    
    for i in range(n-1):
        if case[i] == '+':
            answer += n_list[i+1]
        elif case[i] == '-':
            answer -= n_list[i+1]
        elif case[i] == '*':
            answer *= n_list[i+1]
        elif case[i] == '%': 
            if answer < 0: 
                answer = -(-answer // n_list[i+1])
            else:
                answer //= n_list[i+1]
                
    if answer < min:
        min = answer
    if answer > max:
        max = answer

print(max)
print(min)


# 14889
from sys import maxsize 
from itertools import combinations 
n = int(input()) 
s = [list(map(int, input().split())) for _ in range(n)] 
cb = combinations(range(n), n//2) 
ans = maxsize 

for c in cb: 
  a = set(c) 
  b = list(set(range(n)) - a) 
  a = list(a) 
  
  a_teamwork, b_teamwork = 0, 0 
  for i in range(n//2 - 1): 
    for j in range(i + 1, n//2): 
      a_teamwork += s[a[i]][a[j]] + s[a[j]][a[i]] 
      b_teamwork += s[b[i]][b[j]] + s[b[j]][b[i]] 
  ans = min(ans, abs(b_teamwork - a_teamwork)) 
print(ans)