#include <cstdio>
#include <vector>

using namespace std;

int main(void){

    vector<int> input_n_numbers;

    int T;
    scanf("%d", &T);

    while(T--){
        int N;
        scanf("%d", &N);
        input_n_numbers.push_back(N);
    }

    vector<long long> k(101, 0);

    k[1] = 1;
    k[2] = 1;
    k[3] = 1;
    k[4] = 2;
    k[5] = 2;

    for(int i=6; i<=100; i++){
        k[i] = k[i-1] + k[i-5];
    }

    for(vector<int>::iterator iter = input_n_numbers.begin(); iter!=input_n_numbers.end(); iter++){
        printf("%lld\n", k[*iter]);
    }

    return 0;
}