# 1330
a, b = input().split()
A, B = int(a), int(b)
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')


# 9498
grade = int(input())
if 89 < grade < 101:
    print('A')
elif 79 < grade < 90:
    print('B')
elif 69 < grade < 80:
    print('C')
elif 59 < grade < 70:
    print('D')
else:
    print('F')


# 2753
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)


# 14681
x = int(input())
y = int(input())
if (x > 0 and y > 0):
    print(1)
elif (x < 0 and y > 0):
    print(2)
elif (x < 0 and y < 0):
    print(3)
else:
    print(4)


# 2884
h, m = map(int, input().split())
if m > 44:
    print(h, m - 45)
elif M <= 44 and h >= 1:
    print(h-1, m+15)
else:
    print(23, m+15)