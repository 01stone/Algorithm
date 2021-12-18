def solution(s):
    answer = ''
    s = s.lower().split(" ")

    for i in s:
        for j, k in enumerate(i):
            if j % 2 == 0:        
                k = k.upper()     
            answer += k          
        answer += " "             
    return answer[:-1]