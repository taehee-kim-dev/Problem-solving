"""
ATM

N : 총 사람의 수
i번 사람이 걸리는 시간 = Pi
"""

N = int(input())

P_list = list(map(int, input().split(' ')))

P_list.sort()


for index_of_Pi in range(1, len(P_list)):
    P_list[index_of_Pi] += P_list[index_of_Pi - 1]

print(sum(P_list))
