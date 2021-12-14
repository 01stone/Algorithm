# 1712
'''
trial_1 : 마이너스 값 나오지 않음, 갯수 1개 부족

A, B, C = map(int, input().split())
n = 1
while A + B * n > C * n :
    n += 1
print(n)
'''

A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(int(A / (C - B) + 1))
 

# 2292
num = int(input())
honeycomb = 1
count = 1
while num > honeycomb:
    honeycomb += 6 * count
    count += 1
print(count)
 

# 1193
x = int(input())

num = 0
cnt = 0
while x > num:
    num = num + cnt
    cnt += 1

num_list = []
for i in range(1,cnt):
    num_list.append(i)
num_list_re = list(reversed(num_list))

num_x = num - x
if cnt % 2 == 0:
    print(f'{num_list[num_x]}/{num_list_re[num_x]}')
else:
    print(f'{num_list_re[num_x]}/{num_list[num_x]}')
 

# 2869
'''
trial_1 : 시간 초과
A, B, V = map(int, input().split())
day = 0
height = 0
while True:
    day += 1
    height += A
    if height == V:
        print(day)
        break
    height -= B
'''

import math
A, B, V = map(int, input().split())
print(math.ceil((V - A) / (A - B) + 1))


# 10250
guest = int(input())

for i in range(guest):
    H, W, N = map(int, input().split())
    x = (N - 1) // H + 1
    y = (N - 1) % H + 1
    print(y * 100 + x)
 

# 2775
apt = int(input())
for i in range(apt):
    k = int(input())
    n = int(input())
    k0 = [z for z in range(1, n+1)]
    for a in range(k):
        for b in range(1,n):
            k0[b] += k0[b-1]
    print(k0[-1])
 

# 2839
sugar = int(input())
deli = 0

while True:
    if sugar % 5 == 0:            # 설탕이 5의 배수일 경우
        print(deli + sugar // 5)
        break
    sugar -= 3        # 5의 배수가 될 때까지 3을 빼줌
    deli += 1
    if sugar < 0:   # 3과 5의 배수가 아닐 경우
        print(-1)
        break
 

# 10757
A, B = map(int, input().split())
print(A + B)
 

# 1011
num = int(input())
for i in range(num):
    x, y = map(int, input().split())
    distance = y - x
    cnt = 0       # 이동 횟수
    move = 1      # cnt별 이동 가능한 거리
    move_sum = 0  # 이동한 거리의 합
    while move_sum < distance :
        cnt += 1
        move_sum += move  # cnt에 해당하는 move를 더함
        if cnt % 2 == 0 :  # cnt가 2의 배수일 때, 
            move += 1  
    print(count)