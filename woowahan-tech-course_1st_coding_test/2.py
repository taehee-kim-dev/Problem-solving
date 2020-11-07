

def solution(s, op):
    answer = []

    for i in range(1, (len(s) - 1) + 1):
        left_num = int(s[:i])
        right_num = int(s[i:])

        result = 0
        if op == '+':
            result = left_num + right_num
        elif op == '-':
            result = left_num - right_num
        elif op == '*':
            result = left_num * right_num

        answer.append(result)
    return answer
