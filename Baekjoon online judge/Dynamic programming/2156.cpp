#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){

    int n;

    scanf("%d", &n);

    vector<int> inputs(1, 0);
    vector<int> dp(n+1, 0);

    int t=n;
    while(t--){
        int input;
        scanf("%d", &input);
        inputs.push_back(input);
    }

    dp[1] = inputs[1];
    dp[2] = dp[1]+inputs[2];

    for(int i=3; i<=n; i++){
        dp[i] = max({dp[i-1], inputs[i]+dp[i-2], inputs[i]+inputs[i-1]+dp[i-3]});
    }

    printf("%d", dp[n]);

    return 0;
}