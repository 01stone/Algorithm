# 2448 : 별찍기 - 11

n = int(input())
tree = ["  *  ", " * * ", "*****"]

def fractal(tree):
  length = len(tree)
  for i in range(length):
    tree.append(tree[i] + " " + tree[i])
    tree[i] = " "*length + tree[i] + " "*length
  return tree

cnt = 0
while n>1:
  n//=2
  cnt+=1

for _ in range(cnt-1):
  fractal(tree)

for j in tree:
  print(j)
