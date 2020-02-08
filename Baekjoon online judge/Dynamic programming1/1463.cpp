#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){

    int n;
    scanf("%d", &n);

    vector<int> cases_for_nums(n+1, -1);

    cases_for_nums[0]=0;
    cases_for_nums[1]=0;

    for(int i=2; i<=n; i++){
        cases_for_nums[i]=cases_for_nums[i-1]+1;
        if(i%2==0){
            cases_for_nums[i]=min(cases_for_nums[i], cases_for_nums[i/2]+1);
        }
        if(i%3==0){
            cases_for_nums[i]=min(cases_for_nums[i], cases_for_nums[i/3]+1);
        }
    }

    printf("%d", cases_for_nums[n]);

    return 0;
}