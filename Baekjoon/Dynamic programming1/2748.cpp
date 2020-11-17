#include <cstdio>
#include <vector>

using namespace std;

vector<long long> fib_nums(91, -1);

long long Fibonacci(int n){
    if(fib_nums[n]!=-1)return fib_nums[n];
    return fib_nums[n] = Fibonacci(n-2) + Fibonacci(n-1);
}

int main(void){

    int n;
    scanf("%d", &n);

    fib_nums[0]=0;
    fib_nums[1]=1;

    printf("%lld ", Fibonacci(n));

    return 0;
}