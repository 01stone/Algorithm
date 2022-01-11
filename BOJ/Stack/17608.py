# 17608 : 막대기 bronz_2
'''
높이만 다르고 (같은 높이의 막대기가 있을 수 있음) 모양이 같은 막대기를 일렬로 세운 후, 
왼쪽부터 차례로 번호를 붙인다. 
각 막대기의 높이는 그림에서 보인 것처럼 순서대로 6, 9, 7, 6, 4, 6 이다. 
일렬로 세워진 막대기를 오른쪽에서 보면 보이는 막대기가 있고 보이지 않는 막대기가 있다. 
즉, 지금 보이는 막대기보다 뒤에 있고 높이가 높은 것이 보이게 된다. 
N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하려고 한다.
'''
import sys
input = sys.stdin.readline # 안넣으면 시간초과 뜸

n = int(input())
stk = [int(input()) for _ in range(n)] # 리스트 만듦
see = stk[-1]                # 가장 오른쪽 값
cnt = 1

for i in range(n):
    temp = stk.pop() # 맨 마지막 값 출력, 제거
    if see < temp:   # 봤던 값보다 크면
        cnt += 1     # 1 증가
        see = temp   # see를 지금의 temp(더 큰 값)로 변경

print(cnt)