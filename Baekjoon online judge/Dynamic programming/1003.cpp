#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

vector<long long> fib_nums(41, -1);

long long Fibonacci(int n){
    if(fib_nums[n]!=-1)return fib_nums[n];
    return fib_nums[n] = Fibonacci(n-2) + Fibonacci(n-1);
}

int main(void){

    vector<pair<long long, long long>> result;

    fib_nums[0]=0;
    fib_nums[1]=1;

    int T;
    scanf("%d", &T);
    while(T--){
        int n;
        scanf("%d", &n);

        if(n==0){
            result.push_back(make_pair(1, 0));
        }else if(n==1){
            result.push_back(make_pair(0, 1));
        }else{
            result.push_back(make_pair(Fibonacci(n-1), Fibonacci(n)));
        }
    }

    for(vector<pair<long long, long long>>::iterator iter=result.begin(); iter!=result.end(); iter++){
        printf("%lld %lld\n", (*iter).first, (*iter).second);
    }

    return 0;
}