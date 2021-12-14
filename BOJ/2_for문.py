# 2739
num = int(input())
for i in range(1,10):
    print(f'{num} * {i} = {num * i}')
 

# 10950
cnt = int(input())
for i in range(cnt):
    num1, num2 = map(int, input().split())
    print(num1 + num2)
 

# 8393
n = int(input())
sum = 0
for i in range(n+1):
    sum = sum + i
print(sum)
 

# 2741
n = int(input())
for i in range(1, n+1):
    print(i)
 

# 2742
n = int(input())
for i in range(n):
    print(n-i)
 

# 11021
n = int(input())
for i in range(n):
    num1, num2 = map(int, input().split())
    print(f'Case #{i+1}: {num1 + num2}')
 

# 11022
n = int(input())
for i in range(n):
    num1, num2 = map(int, input().split())
    print(f'Case #{i+1}: {num1} + {num2} = {num1 + num2}')
 

# 2438 
n = int(input())
for i in range(1, n+1):
    print('*' * i)
 

# 2439
n = int(input())
for i in range(1, n+1):
    print(' '* (n-i) + '*' * i)
 

# 10871 
N, X = map(int, input().split())
sequence_list = list(map(int, input().split()))
for i in range(N):
    if sequence_list[i] < X:
        print(sequence_list[i], end=" ")