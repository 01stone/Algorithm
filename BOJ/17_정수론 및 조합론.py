# 5086 : 배수와 약수
while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  if b % a == 0:
    print('factor')
  elif a % b == 0:
    print('multiple')
  else:
    print('neither')


# 2609 : 최대공약수와 최소공배수
from math import gcd

a, b = map(int, input().split())

def lcm(a, b):
  return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))


# 1934 : 최소공배수
from math import gcd

n = int(input())

for _ in range(n):
  a, b = map(int, input().split())

  def lcm(a, b):
    return a * b // gcd(a, b)
  
  print(lcm(a, b))


# 3036 : 링
from math import gcd

n = int(input())
rings = list(map(int, input().split()))

# def gcd(a, b):
#     while(b != 0):
#         n = a%b
#         a = b
#         b = n
#     return a
for i in range(1, n):
  g = gcd(rings[0], rings[i])
  # print(rings[0], rings[i], g, rings[0]//g, rings[i]//g)
  print(f'{rings[0]//g}/{rings[i]//g}')


# 11050 : 이항계수1
# 순열? 그거 공식인듯

from math import factorial
# def factorial(n):
#   if n == 0:
#     return 1
#   return n * factorial(n-1)

n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n-k)))


# 11051 : 이항계수2
from math import factorial

n, k = map(int, input().split())
answer = factorial(n) // (factorial(k) * factorial(n-k))
print(answer%10007)


# 1010 : 다리놓기
# 이항계수랑 똑같은 것 같은디? n하고 k 위치 바꿔야 함!
from math import factorial

t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  print(factorial(k) // (factorial(n) * factorial(k-n)))


# 9375 : 패션왕 신해빈
# 어디서 풀어봤던 건디....
# 프로그래머스 lv2.위장
'''
def solution(clothes):
    answer = 1
    c_list = [i[1] for i in clothes]
    c_set = set(c_list)
    for i in c_set:
        answer *= c_list.count(i)+1
    return answer - 1
'''
t = int(input())
cloth_list = []

for i in range(t):
  n = int(input())
  clothes = []
  for _ in range(n):
    cloth = input().split()
    clothes.append(cloth)
  cloth_list.append(clothes)
# print(cloth_list)

for i in range(len(cloth_list)):
  answer = 1
  cloth_list_day = [j[1] for j in cloth_list[i]]
  cloth_list_day_set = set(cloth_list_day)
  for k in cloth_list_day_set:
    answer *= cloth_list_day.count(k)+1
  print(answer-1)


  # 1676 : 팩토리얼 0의 개수
# 처음에 n까지 팩토리얼 리스트 구해서 어쩌구 함 바보

from math import factorial

n = int(input())

cnt = 0
for i in str(factorial(n))[::-1]:
  if i != '0':
    break
  cnt += 1

print(cnt)


# 2004 : 조합 0의 개수
# cnt_5 = n의 5의 개수 - (k의 5의 개수 + (n-k)의 5의 개수)
# cnt_2 = n의 2의 개수 - (k의 2의 개수 + (n-k)의 2의 개수)
# 둘 중 min 값이..10의 배수니까...0의 개수...
'''
# 시간초과
from math import factorial

def cnt_num(n, cnt_n):
  cnt = 0
  for i in range(1, n+1):
    if i % cnt_n == 0:
      cnt += 1
  return cnt

n, m = map(int, input().split())

cnt_5 = cnt_num(factorial(n), 5) - cnt_num(factorial(m), 5) - cnt_num(factorial(n-m), 5)
cnt_2 = cnt_num(factorial(n), 2) - cnt_num(factorial(m), 2) - cnt_num(factorial(n-m), 2)

print(min(cnt_5, cnt_2))
'''

def cnt_num(n, cnt_n):
  cnt = 0
  while n:
    # print(f'n : {n}')
    n = n // cnt_n    # n까지 cnt_n의 개수
    # print(f'n//cnt_n : {n}')
    cnt += n          # 누적해서 더하면 n!에서 cnt_n의 총합
  return cnt

n, m = map(int, input().split())

cnt_5 = cnt_num(n, 5) - cnt_num(m, 5) - cnt_num(n-m, 5)
cnt_2 = cnt_num(n, 2) - cnt_num(m, 2) - cnt_num(n-m, 2)

print(min(cnt_5, cnt_2))


