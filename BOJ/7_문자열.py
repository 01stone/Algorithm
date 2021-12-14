# 11654
a = input()
print(ord(a))
 

# 11720
n = input()
print(sum(map(int, input())))
 

# 10809
s = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(s.find(chr(i)), end = ' ')
 

# 2675
trial = int(input())
for i in range(trial):
    num, word = input().split()
    result = ''
    for i in word:
        result += int(num)*i
    print(result)
 

# 1157
word = input().upper()
word_set = list(set(word))  

num = []  # 알파벳 당 갯수
for i in word_set :
    num.append(word.count(i))  

if num.count(max(num)) > 1 :
    print('?')
else :
    max_index = num.index(max(num))
    print(word_set[max_index])
 

# 1152
'''
trial_1 : 틀렸습니다!
txt = input()
print(len(txt.split(' ')))
'''
'''
trial_2 : 런타임 에러
txt = input.split
print(len(txt))
'''
print(len(input().split()))
 

# 2908
'''
trial_1 : 런타임에러
A = int(input())
B = int(input())
A = int(A[::-1]) 
B = int(B[::-1])
if A > B:
    print(A)
else:
    print(B)
'''
'''
trial_2 : 런타임에러
A, B = int, input().split()
A = int(A[::-1]) 
B = int(B[::-1])
if A > B:
    print(A)
else:
    print(B)
'''
A, B = input().split()
A = int(A[::-1]) 
B = int(B[::-1])
print(max(A, B))


# 5622
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
sec = 0

for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            sec += dial.index(j) + 3

print(sec)
 

# 2941
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    word = word.replace(i, '*')

print(len(word))
 

# 1316
num = int(input())
count = num

for i in range(num):
    word = input()
    for j in range(len(word)-1):
        if word.find(word[j]) > word.find(word[j+1]):
            count -= 1
            break

print(count)