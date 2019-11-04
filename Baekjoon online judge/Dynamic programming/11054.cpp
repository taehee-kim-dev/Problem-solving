#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){

    int N;

    scanf("%d", &N);

    int T=N;

    vector<int> inputs;
    vector<int> dp_increase(N, 1);
    vector<int> dp_decrease(N, 1);
    vector<int> dp_inc_dec(N, 0);

    while(T--){
        int input;
        scanf("%d", &input);
        inputs.push_back(input);
    }

    for(int i=1; i<N; i++){
        int max=0;
        for(int j=0; j<i; j++){
            if(inputs[j]<inputs[i] && max<dp_increase[j]){
                max=dp_increase[j];
            }
        }
        dp_increase[i] = max+1;
    }

    for(int i=N-2; i>=0; i--){
        int max=0;
        for(int j=N-1; i<j; j--){
            if(inputs[j]<inputs[i] && max<dp_decrease[j]){
                max=dp_decrease[j];
            }
        }
        dp_decrease[i] = max+1;
    }

    for(int i=0; i<N; i++){
        dp_inc_dec[i] = dp_increase[i] + dp_decrease[i]-1;
    }

    printf("%d", *max_element(dp_inc_dec.begin(), dp_inc_dec.end()));

    return 0;
}