n = int(input())
input_list = list(map(int, input().split()))

dp = [0 for i in range(n)]

dp[0] = input_list[0]

for i in range(1, n):
    if dp[i-1] + input_list[i] > input_list[i]:
        dp[i] = dp[i-1] + input_list[i]
    else:
        dp[i] = input_list[i]

print(max(dp))
