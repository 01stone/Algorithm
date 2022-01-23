# 5568 : 카드 놓기

from itertools import permutations  # 코테에서 이용 가능

n = int(input())
k = int(input())
n_list = [input().rstrip() for _ in range(n)]

answer = set()
for i in permutations(n_list, k):
    # print(i, end='')            # ('1', '2')('1', '12')('1', '1')('2', '1')('2', '12')('2', '1')('12', '1')('12', '2')('12', '1')('1', '1')('1', '2')('1', '12')
    # print(''.join(i), end=', ') # 12, 112, 11, 21, 212, 21, 121, 122, 121, 11, 12, 112,
    answer.add(''.join(i))

# print(answer)  # {'21', '11', '122', '112', '121', '12', '212'}
print(len(answer))
