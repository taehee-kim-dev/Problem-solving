"""
2606번
바이러스
"""


def dfs(current_checking_computer_number):
    global total_infected_computer_count

    # 만약 이미 방문한 컴퓨터라면
    if is_visited_computer[current_checking_computer_number]:
        return

    # 새로 방문한 컴퓨터 이므로, 방문했음을 표시
    is_visited_computer[current_checking_computer_number] = True

    # 이전에 방문한 컴퓨터가 아니라면,
    # 현재 검사중인 컴퓨터는 감염되었으므로 총 감염된 컴퓨터의 개수를 1 증가시킨다.
    total_infected_computer_count += 1

    # 현재 검사중인 컴퓨터에 연결된 다른 모든 컴퓨터를 탐색한다.
    for another_linked_computer_number_with_current_checking_computer_number \
            in linked_inform[current_checking_computer_number]:

        dfs(another_linked_computer_number_with_current_checking_computer_number)

    return


total_infected_computer_count = 0

# 컴퓨터의 수 (<= 100)
N = int(input())

# 컴퓨터 상호간 연결 정보
# index : 존재하는 컴퓨터 번호
# linked_inform[index] = [index 컴퓨터 번호의 컴퓨터에 연결된 다른 컴퓨터들의 번호들 리스트]
# 0번 인덱스는 사용하지 않으므로 'X'로 표시
linked_inform = ['X']

# 컴퓨터 각각의 방문 여부
# index : 존재하는 컴퓨터 여부
# is_visited_computer[index] = 해당 컴퓨터를 방문했는지에 대한 True / False 값
# 0번 인덱스는 사용하지 않으므로 'X'로 표시
is_visited_computer = ['X']

for _ in range(N):
    linked_inform.append([])
    is_visited_computer.append(False)

case_count = int(input())

for _ in range(case_count):
    a_computer, b_computer = map(int, input().split())
    linked_inform[a_computer].append(b_computer)
    linked_inform[b_computer].append(a_computer)

dfs(1)

print(total_infected_computer_count - 1)
