# 13771 : presents

li = [input() for _ in range(int(input()))]
li.sort(key=lambda x:float(x))
print(li[1])