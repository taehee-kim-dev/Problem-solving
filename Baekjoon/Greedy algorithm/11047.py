"""
동전 0

종류 : N가지
각 종류의 동전 : 무한대
총 동전 가치의 합 : K
동전 개수를 최소로 써야 함.
가장 큰 금액의 동전부터 나눔.
"""

N, K = map(int, input().split(' '))

A_list = []
for _ in range(N):
    A_list.append(int(input()))

# 가치 내림차순으로 동전 정렬
A_list.sort(reverse=True)

total_coin_count = 0

# 가치가 큰 동전부터 검사
for Ai in A_list:
    # 동전의 가치 Ai가 남은 총 동전 가치 K보다 크면 계산 불가
    # 계산할 수 있는 동전들 중 가장 큰 가치를 가진 동전으로 계산
    if Ai > K:
        continue
    # 총 동전의 개수는 남은 총 가치를 현재 검사하는 동전의 가치로 나눈 몫의 정수값
    total_coin_count += int(K / Ai)
    # 남은 총 가치는 현재 검사하고 있는 동전의 가치로 나눈 나머지 값
    K %= Ai

print(total_coin_count)
