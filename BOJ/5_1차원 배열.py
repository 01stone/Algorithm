# 10818
# 근데 이거 list 갯수 count랑 달라도 에러 안뜸..
count = int(input())
num_list = list(map(int, input().split()))
print(min(num_list), max(num_list))
 

# 2562
num_list = []
for i in range(9):
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)
 

# 2577
A = int(input())
B = int(input())
C = int(input())
num_list = list(str(A*B*C))
for i in range(10):
    print(num_list.count(str(i)))
 

# 3052
num_list = []
for i in range(10):
    n = int(input())
    num_list.append(n % 42)
print(len(set(num_list)))
 

# 1546
sub = int(input())
sub_score = list(map(int, input().split()))
max_score = max(sub_score)

new_score = []
for score in sub_score:
    new_score.append(score/max_score*100)

print(sum(new_score)/sub)
 

# 8958
cnt = int(input())

for _ in range(cnt):
    ox_list = list(input())
    score = 0  
    score_sum = 0
    
    for ox in ox_list:
        if ox == 'O':
            score += 1 
            score_sum += score
        else:
            score = 0
    print(score_sum)
 

# 4344
num = int(input())

for _ in range(num):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]
    
    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt += 1
            
    per = (cnt/scores[0])*100
    print('%.3f' %per + '%')