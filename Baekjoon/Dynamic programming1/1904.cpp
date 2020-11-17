#include <cstdio>
#include <vector>

using namespace std;

int main(void){

    int N;
    scanf("%d", &N);

    vector<int> cases_per_number(1000001, -1);

    cases_per_number[0]=0;
    cases_per_number[1]=1;
    cases_per_number[2]=2;

    for(int i=3; i<=N; i++){
        cases_per_number[i] = (cases_per_number[i-1]+cases_per_number[i-2])%15746;
    }

    printf("%d", cases_per_number[N]);

    return 0;
}