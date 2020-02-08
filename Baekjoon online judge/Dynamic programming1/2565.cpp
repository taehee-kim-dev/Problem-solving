#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const vector<int> &v1, const vector<int> &v2){
    return v1[0]<v2[0];
}

int main(void){

    int N;

    scanf("%d", &N);

    vector<vector<int>> inputs;

    int T=N;

    while(T--){
        int input_A, input_B;
        scanf("%d %d", &input_A, &input_B);
        vector<int> input_tmp;
        input_tmp.push_back(input_A);
        input_tmp.push_back(input_B);

        inputs.push_back(input_tmp);
    }

    sort(inputs.begin(), inputs.end(), compare);

    vector<int> dp(N, 1);

    for(int i=1; i<N; i++){
        int max=0;
        for(int j=0; j<i; j++){
            if(inputs[i][1]>inputs[j][1] && max<dp[j]){
                max = dp[j];
            }
        }
        dp[i] = max + 1;
    }

    printf("%d", N-*max_element(dp.begin(), dp.end()));

    return 0;
}