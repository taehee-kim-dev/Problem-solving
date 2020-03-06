#include <iostream>

#include <string>
#include <vector>

using namespace std;

// 에라토스테네스의 체
int solution(int n) {
    int answer = 0;

    // 숫자(인덱스) 별로 소수 유무를 체크할 bool형 벡터
    // nums[0] ~ nums[n];
    vector<bool> nums(n + 1, true);
    // 0과 1은 소수가 아니므로 false로 초기화
    nums[0] = false;
    nums[1] = false;

    // 2부터 n / 2 + 1까지 
    for(int i = 2; i <= (n / 2 + 1); i++){
        // 소수체크가 되어있는 i의 모든 배수들을 돈다.
        // 배수들은 모두 소수가 아니므로,
        // 만약 소수라고 체크되어있다면 false로 바꾼다.
        if(nums[i] == true){
            for(int j = 2 ; i * j <= n ; j++){
                if(nums[i * j] == true)
                    nums[i * j] = false;
            }
        }
    }

    // nums vector에서 true의 갯수를 센다.
    for(int i = 2; i < nums.size(); i++){
        if(nums[i] == true)
            answer++;
    }

    return answer;
}

int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int answer = solution(10);
    cout<<answer;

    return 0;
}