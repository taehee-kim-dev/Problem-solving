#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(long long n) {
    long long answer = 0;

    if(floor(sqrt(n)) == sqrt(n)){
        // 어떤 양의 정수 x의 제곱이라면,
        answer = (long long)(pow(sqrt(n) + 1.0, 2.0));
    }else{
        answer = -1;
    }

    return answer;
}