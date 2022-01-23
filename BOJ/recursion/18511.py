# 18511 : 큰 수 구성하기

from itertools import product

n, k = map(int, input().split())
k_list = list(map(str, input().split()))
length = len(str(n))

while True:
    k_list_p = list(map(''.join, product(k_list, repeat = length)))
    answer = []
    for i in k_list_p:
        if int(i) <= n:
            answer.append(i)
    if len(answer) >= 1:
        print(max(answer))
        break
    else:
        length -= 1