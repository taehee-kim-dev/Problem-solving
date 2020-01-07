N, K = map(int, input().split())

W = [0 for w in range(N+1)]
V = [0 for v in range(N+1)]

for i in range(1, N+1):
    w, v = map(int, input().split())
    W[i] = w
    V[i] = v

dp = [[0 for col in range(K+1)] for row in range(N+1)]

for i in range(1, N+1):
    for j in range(K+1):
        dp[i][j] = dp[i-1][j]
        if W[i] <= j:
            dp[i][j] = max(dp[i][j], dp[i-1][j-W[i]]+V[i])

print(dp[N][K])
