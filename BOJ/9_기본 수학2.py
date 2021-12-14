# 1978
n = int(input())
nums = map(int, input().split())

prime_num = 0
for num in nums:
    com_num = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                com_num += 1
        if com_num == 0:
            prime_num += 1
print(prime_num)
 

# 2581
'''
trial_1 : 시간 초과
m = int(input())
n = int(input())
prime_list = []

for number in range(m,n+1):
    com_num = 0
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                com_num += 1
        if com_num == 0:
            prime_list.append(number)
            
if prime_list == []:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))
'''

'''
trial_2 : 시간 초과

for num in range(m,n+1):
    com_num = 0
    if num == 1: 
        continue
    for i in range(2, num+1):
        if num % i == 0:
            com_num += 1
    if com_num == 1:
        prime_list.append(num)
        
if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))
'''

'''
trial_3 : 틀렸습니다!

for num in range(m,n+1):
    if num == 1:
        pass
    elif num == 2:
        prime_list.append(num)
    else:
        for i in range(2, num):
            if num % i == 0:
                break
            elif num == i - 1:
                prime_list.append(i)
'''

m = int(input())
n = int(input())
prime_list = []

for num in range(m,n+1):
    com_num = 0
    for i in range(1, num+1):
        if num % i == 0:
            com_num += 1
            if com_num > 2:  # 2개 초과면 합성수이므로 계산 끛
                break
    if com_num == 2:
        prime_list.append(num)

if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))
 

# 11653
n = int(input())
p = 2
while n != 1:
    if n % p == 0:
        n = n/p
        print(p)
    else:
        p += 1


# 1929
'''
trial_1 : 시간초과
m, n = map(int, input().split())
prime_list = []

for num in range(m,n+1):
    com_num = 0
    for i in range(1, num+1):
        if num % i == 0:
            com_num += 1
            if com_num > 2:  # 2개 초과면 합성수이므로 계산 끛
                break
    if com_num == 2:
        prime_list.append(num)

for i in prime_list:
    print(i)
'''

# 에라토스테네스의 체 : n개까지 수 중 소수는 n**0.5 까지 존재함

def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

m, n = map(int, input().split())
for i in range(m, n+1):
    if is_prime(i):
        print(i)
 

# 4948
'''
trial_1 : 틀렸습니다
def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

prime_list = []
for i in range(123456):
    if is_prime(i):
        prime_list.append(i)
        
while(1):
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in prime_list:
        if n < i <= n*2:
            cnt += 1
    print(cnt)
'''

def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

all_list = list(range(2,246912))
prime_list = []
for i in all_list:
    if is_prime(i):
        prime_list.append(i)

while(1):
    answer = 0
    n = int(input())
    if n == 0: break

    for i in prime_list:
        if n < i <= n*2:
            answer += 1

    print(answer)
 

# 9020
'''
trial_1 : 컴파일에러
def Goldbach():
    check = [False, False] + [True] * 10000  #  0, 1 : False, 10001까지 리스트
    
    for i in range(2, 101):  # 에라토스어쩌구 4 ~ 10000 범위 숫자
         if check[i] == True:                 # 2부터
            for j in range(i + i, 10001, i):  # 배수는
                check[j] = False              # 제거함

    T = int(input())   # for문 횟수
    for _ in range(T):
        n = int(input())
        A = n // 2   # 어차피 넣을 값이 짝수니까...ㅉ...
        B = A        # 굳이 절반을 나눈 이유는 차이가 최소를 찾아야 하기 때문
        for _ in range(10000):
            if check[A] and check[B]:   # A와 B가 소수면 출력
                print(A, B)
                break
            A -= 1
            B += 1

Goldbach()
'''
check = [False, False] + [True] * 10000  
    
for i in range(2, 101):
     if check[i] == True:
        for j in range(i + i, 10001, i):
            check[j] = False

T = int(input())
for j in range(T):
    n = int(input())
    A = n // 2
    B = A
    for k in range(10000):
        if check[A] and check[B]:
            print(A, B)
            break
        A -= 1
        B += 1


# 1085
'''
trial_1 : 틀렸습니다
x, y, w, h = map(int, input().split())

d_list = []

if x < w/2:
    d_list.append(x)
else:
    d_list.append(w-x)
    
if y < h/2:
    d_list.append(y)
else:
    d_list.append(h-y)    

    print(min(d_list))
'''

x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))
 

# 3009
x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x_4 = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y_4 = y_list[i]

print(x_4, y_4)
 

# 4153
while True:
    pythagoras = list(map(int, input().split()))
    if sum(pythagoras) == 0:
        break
    max_leg = max(pythagoras)
    pythagoras.remove(max_leg)
    if pythagoras[0]**2 + pythagoras[1]**2 == max_leg**2:
        print('right')
    else:
        print('wrong')
 

# 3053
'''
trial_1 : 틀렸습니다
r = int(input())
pi = 3.141592
print(r*r*pi)
print(2*r*r)
'''

import math
r = int(input())
print(r*r*math.pi)
print(2*r*r)
 

# 1002
cnt = int(input())

for _ in range(cnt):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    
    if r1 > d + r2 or r2 > d + r1 or d > r1 + r2:
        print(0)
    elif r1 == d + r2 or r2 == d + r1 or r1 + r2 == d:
        print(1)
    else:
        print(2)