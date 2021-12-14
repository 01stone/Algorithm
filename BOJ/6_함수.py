# 15596
def solve(a):
    return sum(a)
 

# 4673
def d(n): # 생성자 함수
    n = n + sum(map(int, str(n)))
    return n

d_list = [] # 생성자 리스트
for cnt in range(10001):
    d_list.append(d(cnt))
d_list.sort()

for cnt in range(1,10000): # 셀프넘버 출력
    if cnt in d_list: 
        continue
    else:
        print(cnt)
 

# 1065
num = int(input())

hansu = 0
for n in range(1, num+1):
    num_list = list(map(int, str(n)))
    if n < 100: 
        hansu += 1  # 100보다 작으면 무조건 한수
    elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
        hansu += 1  # 100보다 크면 자리수 차이가 같으면 한수
print(hansu)