# 10952 
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)
 

# 10951
'''
trial_1 : 런타임에러
while True:
    a, b = map(int, input().split())
    print(a + b)
'''
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
 

# 1110
n_input = int(input())
n = n_input
cnt = 0
while True:
    n_sum = (n // 10) + (n % 10)  # 각 자릿수를 더한수
    n_new = ((n % 10) * 10) + (n_sum % 10)  # 새로 만들어지는 수
    cnt += 1  # 사이클 카운트
    if n_new == n_input:
        break
    n = n_new  # num 변수에 last_num을 지정 
print(cnt)