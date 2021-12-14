# 2798
n, m = map(int, input().split())
n_list = list(map(int, input().split()))
cnt = len(n_list)
sum = 0

for i in range(0, cnt-2):
    for j in range(i+1, cnt-1):
        for k in range(j+1, cnt):
            if n_list[i] + n_list[j] + n_list[k] > m:
                continue
            else:
                sum = max(sum, n_list[i] + n_list[j] + n_list[k])
print(sum)


# 2231
'''
trial_1 : 정신차리자...거꾸로 구했잖ㅇ..어쩐지 쉽더라..
n = int(input())
s_list = list(str(n))
n_list = []
for i in range(len(s_list)):
    n_list.append(int(s_list[i]))   
print(n + sum(n_list))
'''

n = int(input())
result = 0
for i in range(1, n+1):  # 1부터 n까지
    div_n_list = list(map(int, str(i)))  # 각 자리수 리스트
    sum_n = i + sum(div_n_list)  # 분해합
    if sum_n == n:  # 분해합 = n
        result = i  # 네놈이다..
        break
print(result)


# 7568
n = int(input())
s_list = []

for k in range(n):
    w, h = map(int, input().split())
    s_list.append((w, h))

for i in s_list:
    rank = 1
    for j in s_list:
        if i[0] < j[0] and i[1] < j[1]:  # w, h 모두 본인보다 큰 사람
                rank += 1  # 덩치등수는 w, h 모두 큰 사람이므로
    print(rank, end = " ")


# 1018
n, m = map(int, input().split())
l = []
mini = []

for _ in range(n):
    l.append(input())

for a in range(n - 7):
    for i in range(m - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):              # 8X8 범위를 B와 W로 번갈아가면서 검사
                if (j + b)%2 == 0:
                    if l[b][j] != 'W': 
                        idx1 += 1  
                    if l[b][j] != 'B': 
                        idx2 += 1
                else :
                    if l[b][j] != 'B': 
                        idx1 += 1
                    if l[b][j] != 'W': 
                        idx2 += 1
        mini.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        mini.append(idx2)                          # B로 시작했을 때 칠해야 할 부분

print(min(mini))                                   # 칠해야 하는 개수의 최소값


# 1436
'''
trial_1 : 틀렸습니다
n = int(input())
n_str = str(n-1)
print(f'{n_str}666')
'''

n = int(input())
six = 666
cnt = 0
while True:
    if '666' in str(six):
        cnt += 1         # 666 들어가면 count
    if cnt == n:
        print(six)       # n = count 출력
        break
    six += 1             # 666부터 숫자 1씩 증가