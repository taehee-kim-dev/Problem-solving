#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){

    int N;
    scanf("%d", &N);
    int T=N;

    vector<int> inputs;
    vector<int> dp(N, 1);

    while(T--){
        int input;
        scanf("%d", &input);
        inputs.push_back(input);
    }

    for(int i=0; i<N; i++){
        int max=0;
        for(int j=0; j<i; j++){
            if(inputs[j]<inputs[i] && max<dp[j])
                max = dp[j];
        }
        dp[i]+=max;
    }

    printf("%d", *max_element(dp.begin(), dp.end()));

    return 0;
}