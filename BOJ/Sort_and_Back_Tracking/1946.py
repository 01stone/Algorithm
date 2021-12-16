# 1946

n = int(input())

for _ in range(n):
  applicant = int(input())
  score = [0 for _ in range(applicant)] # 0으로 인원만큼 초기화
  count = 1 # 한명은 무조건 뽑기 때문에 1로 초기화

  for _ in range(applicant):
    resume, interview = map(int, input().split())
    score[resume-1] = interview

  min = score[0]

  for i in range(1, applicant): 
    if score[i] < min: # 최솟값이 더 클 경우 1을 증가
      count += 1
      min = score[i]

  print(count)