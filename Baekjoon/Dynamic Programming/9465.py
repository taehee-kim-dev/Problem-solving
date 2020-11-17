import copy

T = int(input())

for _ in range(T):

    sticker = []

    n = int(input())

    for _ in range(2):
        line = [0]
        line.extend(list(map(int, input().split(' '))))
        sticker.append(line)

    dp = copy.deepcopy(sticker)

    for sticker_index in range(2, n + 1):
        dp[0][sticker_index] = max(dp[1][sticker_index - 2], dp[1][sticker_index - 1]) \
                               + sticker[0][sticker_index]

        dp[1][sticker_index] = max(dp[0][sticker_index - 2], dp[0][sticker_index - 1]) \
                               + sticker[1][sticker_index]

    print(max(dp[0][n], dp[1][n]))
