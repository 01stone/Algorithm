# 10828	: 스택 silver_4
'''
정수를 저장하는 스택을 구현한 다음, 
입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.
- push X: 정수 X를 스택에 넣는 연산이다.
- pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
      만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 스택에 들어있는 정수의 개수를 출력한다.
- empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
- top: 스택의 가장 위에 있는 정수를 출력한다. 
      만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys
input = sys.stdin.readline # 안넣으면 시간초과 뜸

stk = []

for i in range(int(input())):
    command = input().split()

    if command[0] == 'push':
        stk.append(command[1])
    
    elif command[0] == 'pop':
        if not stk:
            print(-1)
        else:
            print(stk.pop())
    
    elif command[0] == 'size':
        print(len(stk))
    
    elif command[0] == 'empty':
        if not stk:
            print(1)
        else:
            print(0)
    
    elif command[0] == 'top':
        if not stk:
            print(-1)
        else:
            print(stk[-1])



# 10773	: 제로 silver_4
'''
재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 
가장 최근에 재민이가 쓴 수를 지우게 시킨다.
재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 
'''
import sys
input = sys.stdin.readline # 안넣으면 시간초과 뜸

def sum(n_list): # sum 구현
    sum = 0
    for i in n_list:
        sum += i
    return(sum)

stk = []
for _ in range(int(input())):
    num = int(input())
    
    if num == 0:        # 0일때 바로 직전에 넣은 값 pop
        stk.pop()
    else:
        stk.append(num) # 아니면 스택에 추가

print(sum(stk))



# 9012 : 괄호 silver_4
'''
괄호 문자열(Parenthesis String, PS) : ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자
올바른 괄호 문자열(Valid PS, VPS) : 괄호의 모양이 바르게 구성된 문자열 
기본 VPS : 한 쌍의 괄호 기호로 된 “( )” 문자열

만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 
          “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 
'''
# 4949 균형잡힌 세상과 같은 풀이

for i in range(int(input())):
    ps = input()
    stk = []

    for bracket in ps:
        if (bracket == '('):
            stk.append('(')
        elif bracket == ')':
            if (len(stk) != 0) and (stk[-1]=='('):
                stk.pop()
            else:
                stk.append(')')
                break

    if not stk:
        print('YES')
    else:
        print('NO')



# 4949 : 균형잡힌 세상 silver_4
'''
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 
문자열이 균형을 이루는 조건은 아래와 같다.

- 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다. : ()
- 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다. : []
- 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
- 모든 괄호들의 짝은 1:1 매칭만 가능하다. 
  즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
- 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다. : 공백이 짝수개?

문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.
'''
# 문자열은...모르겠음...
# 일단...괄호들만 스택에 넣어보는걸로.
# 짝괄호 있으면 빼버리고 아니면 남겨서...뭐 해봄


while True:
    sentence = input()
    stk = []

    if sentence == '.':  # while문 정지 조건
        break

    for char in sentence:
        
        if (char == '[') or (char == '('): # 시작하는 괄호는 일단 넣음
            stk.append(char)
        
        elif char == ']':               # 닫는 괄호는 빈스택이 아니고 시작하는 짝괄호가 있으면 같이 소거
            if (len(stk) != 0) and (stk[-1]=='['):
                stk.pop()
            else:                    # 빈 스택이고, 짝괄호가 없으면 넣음
                stk.append(']')
                break
        
        elif char == ')':              
            if (len(stk) != 0) and (stk[-1]=='('):
                stk.pop()
            else:                   
                stk.append(')')
                break
    
    if len(stk) == 0:
        print('yes')
    else: 
        print('no')




'''
sentence = list(input())

bracket_s_l = sentence.count('(')
bracket_s_r = sentence.count(')')
bracket_b_l = sentence.count('[')
bracket_b_r = sentence.count(']')

if (bracket_s_l == bracket_s_r) and (bracket_b_l == bracket_b_r):
    print('yes')
else:
    print('no')

# 괄호 순서가 바뀌어도 yes라고 출력됨..
'''



# 1874 : 스택 수열 silver_3
'''
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

hint) 1부터 n까지에 수에 대해 차례로 
[push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 
연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.
4      []              > []
  push [1]             > []
  push [1, 2]          > []
  push [1, 2, 3]       > []
  push [1, 2, 3, 4]    > []
  pop  [1, 2, 3]       > [4]
3 pop  [1, 2]          > [4, 3]
6 push [1, 2, 5]       > [4, 3]
  push [1, 2, 5, 6]    > [4, 3]
8 pop  [1, 2, 5]       > [4, 3, 6]
  push [1, 2, 5, 7]    > [4, 3, 6]
  push [1, 2, 5, 7, 8] > [4, 3, 6]
7 pop  [1, 2, 5, 7]    > [4, 3, 6, 8]
5 pop  [1, 2, 5]       > [4, 3, 6, 8, 7]
2 pop  [1, 2]          > [4, 3, 6, 8, 7, 5]
1 pop  [1]             > [4, 3, 6, 8, 7, 5, 2]
  pop  []              > [4, 3, 6, 8, 7, 5, 2, 1]
'''
import sys
input = sys.stdin.readline

n = int(input())
stk = []
operators = []
cnt = 0
x = True

for i in range(n):
    num = int(input())
    
    # while i <= num: # 무한루프 돌고있음...안됨...
    while cnt < num: 
        cnt += 1        # 일단 4까지는 넣음
        stk.append(cnt)
        operators.append('+')
    
    if stk[-1] == num:
        stk.pop()
        operators.append('-')
    else:               # 수열이 불가능한 경우
        x = False 
        break         

if x == False: # len(stk) != n 으로 하면 No...
    print('NO') # 이거 NO 대문자...왜 틀리나 했네....
else:
    for j in operators:
        print(j)

