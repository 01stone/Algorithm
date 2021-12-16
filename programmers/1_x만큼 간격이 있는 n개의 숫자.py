def solution(x, n):
    answer = []
    for i in range(int(n)):
        answer.append((i+1) * int(x))
    return answer