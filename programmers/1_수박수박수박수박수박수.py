def solution(n):
    answer = ''
    word_odd = '수'
    word_even = '박'
    for i in range(n):
        if i % 2 == 0:
            answer += word_odd
        else:
            answer += word_even
    return answer
