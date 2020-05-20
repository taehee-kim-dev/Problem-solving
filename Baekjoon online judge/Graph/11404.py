"""
플로이드

도시 : n개
버스 : m개
도시 이동 비용 최솟값?
"""

N_MAX = 100
M_MAX = 1000000

'''
row = from_city
col = to_city
cost_graph[from_city][to_city] = cost
'''
cost_graph = [[0 for _ in range(N_MAX + 1)] for _ in range(N_MAX + 1)]

N = int(input())
M = int(input())

for _ in range(M):
    from_city, to_city, cost = map(int, input().split(' '))

    # 해당 칸에 기존 값이 없으면 그냥 대입
    if not cost_graph[from_city][to_city]:
        cost_graph[from_city][to_city] = cost
    else:
        # 해당 칸에 기존 값이 존재하면, 더 작은 값으로 대입
        cost_graph[from_city][to_city] = min(cost_graph[from_city][to_city], cost)

# 경유 도시 검사
for via in range(1, N + 1):

    # 출발 도시
    for from_city in range(1, N + 1):

        # 애초에 시작도시부터 경유도시까지 갈 수 없으면 건너 뜀.
        if not cost_graph[from_city][via]:
            continue

        # 도착 도시
        for to_city in range(1, N + 1):

            # 경유도시부터 도착도시까지 갈 수 없으면 건너 뜀.
            # 시작도시와 도착 도시가 같은 경우도 건너 뛴다.
            if not cost_graph[via][to_city] or from_city == to_city:
                continue

            '''
            이전에 갈 수 없다고 판단된 경로였거나,
            기존 금액보다 현재 경로의 금액이 더 쌀 경우,
            현재 경로의 금액으로 업데이트
            '''
            if not cost_graph[from_city][to_city] \
                    or cost_graph[from_city][to_city] > cost_graph[from_city][via] + cost_graph[via][to_city]:
                cost_graph[from_city][to_city] = cost_graph[from_city][via] + cost_graph[via][to_city]

# 정답 출력
for from_city in range(1, N + 1):
    for to_city in range(1, N + 1):
        print(cost_graph[from_city][to_city], end=' ')
    print()
