


from queue import PriorityQueue

def solution(n):
    answer = []

    if len(str(n)) == 1:
        return [0, n]

    priority_queue = PriorityQueue()
    # [횟수, 숫자]
    n = str(n)

    for index, num_char in enumerate(n):
        if index < len(n) - 1 and n[index + 1] != '0':
            first = n[:index + 1]
            second = n[index + 1:]
            s = int(first) + int(second)
            priority_queue.put([1, str(s)])


    while not priority_queue.empty():
        num_inform = priority_queue.get()
        if len(num_inform[1]) == 1:
            answer = [num_inform[0], int(num_inform[1])]
            return answer

        for index, num_char in enumerate(num_inform[1]):
            if index < len(num_inform[1]) - 1 and num_inform[1][index + 1] != '0':
                first = num_inform[1][:index + 1]
                second = num_inform[1][index + 1:]
                s = int(first) + int(second)
                priority_queue.put([num_inform[0] + 1, str(s)])


    return answer








print(solution(
73425
))
# [4, 3]

print(solution(
10007
))
# [4, 8]

print(solution(
9
))
# [0, 9]
