# 10872
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))
 

# 10870
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))


# 2447
n = int(input())

stars = ['***', '* *', '***']

cnt = 0
while n > 3:  # n이 3보다 클 경우 제곱수를 찾아내 cnt에 반영
    n = n / 3
    cnt += 1
    
def makeStar():
    star_list = []
    for i in range(len(stars)*3):
        if i // len(stars) == 1: # 가운데 빈칸
            star_list.append(stars[i%len(stars)] + " "*len(stars) + stars[i%len(stars)])
        else:  # 빈칸 없이 첫 모양으로 채워넣음
            star_list.append(stars[i%len(stars)] * 3)
            # stars[0] * 3 >> stars[1] * 3 >> stars[2] * 3    >> 반복
            # '***''***''***'/'* *''* *''* *'/'***''***''***' >> 반복 
    return star_list

for i in range(cnt):
    stars = makeStar()

for star in stars:
    print(star)


# 11729
'''
trial_1 : 틀렸습니다
def hanoi(n, start_poll, pass_poll, goal_poll):
    if n == 1:
        print(start_poll, goal_poll)  
    else:       
        hanoi(n-1, start_poll, goal_poll, pass_poll)
        print(start_poll, goal_poll)
        hanoi(n-1, pass_poll, start_poll, goal_poll)        
n = int(input())
print(2**n - 1)
print(hanoi(n, 1, 2, 3))
'''        

def hanoi(n, start_poll, pass_poll, goal_poll):
    if n == 1:
    	# 원반이 하나면 바로 마지막 기둥으로
        print(start_poll, goal_poll)  
    else:
        # 원반이 여러개면 가장 큰 원반을 제외하고 가운데 기둥으로
        hanoi(n-1, start_poll, goal_poll, pass_poll)
        # 가장 큰 원반이 마지막 기둥으로
        print(start_poll, goal_poll)
        # 가운데 기둥에 있던 원반을 마지막 기둥으로
        hanoi(n-1, pass_poll, start_poll, goal_poll)
        
n = int(input())
print(2**n - 1)
hanoi(n, 1, 2, 3)