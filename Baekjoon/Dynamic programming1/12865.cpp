#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){

    int N, K;
    vector<int> W(1, 0);
    vector<int> V(1, 0);

    scanf("%d %d", &N, &K);

    vector<vector<int>> dp(N+1, vector<int>(K+1, 0));

    int T = N;
    while(T--){
        int w;
        int v;
        scanf("%d", &w);
        scanf("%d", &v);
        W.push_back(w);
        V.push_back(v);
    }

    for(int i=1; i<=N; i++){
        for(int j=0; j<=K; j++){
            dp[i][j] = dp[i-1][j];
            if(j >= W[i]){
                dp[i][j] = max(dp[i][j], dp[i-1][j-W[i]] + V[i]);
            }
        }
    }

    printf("%d", dp[N][K]);

    return 0;
}