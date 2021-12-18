def solution(n):
    answer = [i for i in range(2, n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if i in answer:
            answer = list(set(answer) - set(range(i * 2, n + 1, i)))
    return len(answer)