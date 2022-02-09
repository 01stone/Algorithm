# 10816 : 숫자 카드 2
'''
숫자 카드 : 정수 하나가 적혀져 있는 카드 
숫자 카드 N개를 갖고, 정수 M개가 주어졌을 때, 
이 수가 적혀있는 숫자 카드를 몇 개 가지고 있는지 구하는 프로그램 작성
'''
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_count = Counter(n_list)

for i in m_list:
    if i in n_count:
        print(n_count[i], end=' ')
    else:
        print(0, end=' ')