# 정수 삼각형

N = int(input())
dp = []

for input_line in range(N):
    dp.append(list(map(int, input().split(' '))))

for current_line in range(1, N):
    for current_col_index in range(len(dp[current_line])):

        # 현재 수가 현재 라인의 맨 왼쪽 수일 때,
        if current_col_index == 0:
            # 위 라인의 맨 왼쪽 값이 됨.
            dp[current_line][current_col_index] += dp[current_line - 1][current_col_index]
            continue

        # 현재 수가 현재 라인의 맨 오른쪽의 수일 때,
        if current_col_index == len(dp[current_line]) - 1:
            # 위 라인의 맨 오른쪽 값이 됨.
            dp[current_line][current_col_index] += dp[current_line - 1][current_col_index - 1]
            continue

        # 위의 두 경우가 아니라면,
        # 왼쪽 위 대각선, 오른쪽 위 대각선 중에서 큰 값을 더해야 함.
        dp[current_line][current_col_index] += max(dp[current_line - 1][current_col_index - 1],
                                                   dp[current_line - 1][current_col_index])

print(max(dp[N - 1]))
