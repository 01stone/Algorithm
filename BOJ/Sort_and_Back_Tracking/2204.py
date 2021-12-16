# 2204 : 도비의 난독증 테스트

while True:
  n = int(input())
  voca = []
  if n == 0:
    break
  for i in range(n):
    voca.append(input())
  voca.sort(key=str.lower)
  print(voca[0])