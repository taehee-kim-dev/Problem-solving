#include <iostream>

#include <string>
#include <vector>

using namespace std;

/*
    1  -> xx1
    2  -> xx2
    3  -> xx4

    4  -> x11
    5  -> x12
    6  -> x14

    7  -> x21
    8  -> x22
    9  -> x24

    10 -> x41
    11 -> x42
    12 -> x44

    13 -> 111
    14 -> 112
    15 -> 114

*/


string solution(int n) {
    string answer = "";

    // 현재 자리수에는 1들의 묶음, 2들의 묶음, 4들의 묶음 순으로 각 수들의 묶음이
    // 순서대로, 순환적으로 나열되어 있다. n은 각 묶음들의 총 개수.
    // n이 0보다 큰 동안(현재 자리수에 수가 존재하는 동안) 반복한다.
    while(n > 0){
        // n을 3으로 나눈 나머지를 구한다.
        int r = n % 3;
        if(r == 0){
            // 나머지가 0인 경우,
            // 현재 자리의 수가 순환 반복 단위의 끝 수인 경우이다.
            // 반복 단위에서 마지막 수는 4에 해당하므로, 정답의 맨 앞에 4를 추가한다.
            answer = "4" + answer;
            // 현재 자리수에서 3개의 묶음이 다음 자리수의 하나의 수의 묶음이므로,
            // n / 3 의 값은,
            // 다음 앞자리의 수가 1들의 묶음, 2들의 묶음, 4들의 묶음 순으로
            // 각 수의 묶음들이 총 몇 개 있는지가 된다.
            // 하지만 n/3 이후에 1을 빼줘야 한다.
            // 왜냐하면 현재 자리수 묶음들의 한 번의 순환이
            // 다음 자리수에서 맨 앞에 한 번 없기 때문이다.
            n /= 3;
            n -= 1;
        }else{
            /*
                나머지가 0이 아닌 경우, 즉 3으로 나누어 떨어지지 않는 경우.
                이 경우는 현재 자리의 수가 반복 단위의 끝인 수가 아닌 경우이다.
                n % 3의 값은 현재 자리수의 수 이므로, 정답의 맨 앞에 이 값을 추가한다.
            */
            answer = to_string(n % 3) + answer;
            /*
                현재 자리수에서 3개의 묶음이 다음 자리수의 하나의 수의 묶음이므로,
                n / 3 의 값은,
                다음 앞자리의 수가 1들의 묶음, 2들의 묶음, 4들의 묶음 순으로
                각 수의 묶음들이 총 몇 개 있는지가 된다.
                3으로 나누어 떨어지지 않아 소수점 이하의 자리수가 생기지만, 정수간의 연산으로 인해 버려지므로
                -1을 할 필요가 없다.
            */
           n /= 3;
        }
    }

    return answer;
}

int main(void){

    for(int i = 0; i < 30; i++){
        cout<<solution(i)<<endl;
    }

    return 0;
}