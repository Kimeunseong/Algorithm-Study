# 백준 9012: 괄호

def solution(s):
    while len(s) != 0:
        if s[0] == ')' or s[-1] == '(' or len(s) % 2 == 1:
            return 'NO'
            break
        for i in range(len(s)):
            if i == len(s) - 1:
                break
            elif s[i] == '(' and s[i+1] == ')':
                s = s[:i] + s[i+2:]
                break
        if len(s) == 0 :
            return 'YES'

for i in range(int(input())):
    print(solution(input()))