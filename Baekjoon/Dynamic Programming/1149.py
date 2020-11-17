"""
RGB 거리

i = i번째 집

0 = red
1 = green
2 = blue

i 번 째 집에 red 를 칠할 때의 최소 비용 =
i 번 째 집에 red 를 칠할 때의 비용 +
바로 앞집의 색깔로 올 수 있는 색들의 가격 중 최소값

dp[i][0] = cost_list_of_all_rgb_of_all_house[i][0] + min(dp[i - 1][1], dp[i - 1][2]
"""

cost_list_of_all_rgb_of_all_house = []

N = int(input())

for _ in range(N):
    cost_list_of_all_rgb_of_all_house.append(list(map(int, input().split(' '))))

# 맨 처음 집을 r, g, b로 칠할 때의 총 최소 비용은,
# 맨 처음 집을 r, g, b로 칠할 때의 비용.
dp_min_cost_list_of_rgb_of_all_house = [[0, 0, 0] for _ in range(1000)]

dp_min_cost_list_of_rgb_of_all_house[0] = cost_list_of_all_rgb_of_all_house[0]

for index_of_house in range(1, N):
    # i번 째 집에 red 을 칠할 경우, 첫 번째 집 부터 현재 집 까지의 총 최소 비용
    # 일단 i번 째 집에 red 을 칠할 때 드는 비용
    # 직전의 집 색깔은 green, blue 중의 하나가 와야 한다.
    # 두 경우의 각각 총 최소비용 중 작은 값을 더한다.
    # 그 값의 색깔이 직전 집의 색깔이 됨.
    dp_min_cost_list_of_rgb_of_all_house[index_of_house][0] \
        = cost_list_of_all_rgb_of_all_house[index_of_house][0] \
        + min(
            dp_min_cost_list_of_rgb_of_all_house[index_of_house - 1][1],
            dp_min_cost_list_of_rgb_of_all_house[index_of_house - 1][2]
        )

    # i번 째 집에 green 을 칠할 경우, 첫 번째 집 부터 현재 집 까지의 총 최소 비용
    # 일단 i번 째 집에 green 을 칠할 때 드는 비용
    # 직전의 집 색깔은 red, blue 중의 하나가 와야 한다.
    # 두 경우의 각각 총 최소비용 중 작은 값을 더한다.
    # 그 값의 색깔이 직전 집의 색깔이 됨.
    dp_min_cost_list_of_rgb_of_all_house[index_of_house][1] \
        = cost_list_of_all_rgb_of_all_house[index_of_house][1] \
        + min(
            dp_min_cost_list_of_rgb_of_all_house[index_of_house - 1][0],
            dp_min_cost_list_of_rgb_of_all_house[index_of_house - 1][2]
        )

    # i번 째 집에 blue 을 칠할 경우, 첫 번째 집 부터 현재 집 까지의 총 최소 비용
    # 일단 i번 째 집에 blue 을 칠할 때 드는 비용
    # 직전의 집 색깔은 red, green 중의 하나가 와야 한다.
    # 두 경우의 각각 총 최소비용 중 작은 값을 더한다.
    # 그 값의 색깔이 직전 집의 색깔이 됨.
    dp_min_cost_list_of_rgb_of_all_house[index_of_house][2] \
        = cost_list_of_all_rgb_of_all_house[index_of_house][2] \
        + min(
            dp_min_cost_list_of_rgb_of_all_house[index_of_house - 1][0],
            dp_min_cost_list_of_rgb_of_all_house[index_of_house - 1][1]
        )

print(min(dp_min_cost_list_of_rgb_of_all_house[N - 1]))
