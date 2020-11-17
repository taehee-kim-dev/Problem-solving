#include <cstdio>
#include <vector>
#include <utility>
#include <cmath>

using namespace std;

int main(void){

    // index = 등수, 원소값 = 해당 index의 상금
    // a_rewards = 제1회 코드 페스티벌
    // b_rewards = 제2회 코드 페스티벌
    // 본선진출 실패의 경우 인덱스 0의 원소값은 0
    vector<int> a_rewards(1, 0);
    vector<int> b_rewards(1, 0);

    // i=등수, j=인원
    for(int i=1; i<=6; i++){
        for(int j=1; j<=i; j++){
            // 등수 조건에 따라 해당 인원만큼씩 상금 삽입
            if(i==1)
                a_rewards.push_back(5000000);
            else if(i==2)
                a_rewards.push_back(3000000);
            else if(i==3)
                a_rewards.push_back(2000000);
            else if(i==4)
                a_rewards.push_back(500000);
            else if(i==5)
                a_rewards.push_back(300000);
            else if(i==6)
                a_rewards.push_back(100000);
        }
    }

    // 상금을 못받는 나머지 순위에 대해서 0원으로 대입
    for(int i=22; i<=100; i++)
        a_rewards.push_back(0);


    // i=등수, j=인원
    for(int i=1; i<=5; i++){
        // 인원이 2의 i-1제곱씩 증가함
        for(int j=1; j<=int(pow(2.0, double(i-1))); j++){
                // 상금은 모든 등수가 2의 (10-등수)제곱값과 같음
                b_rewards.push_back(int(pow(2.0, double(10-i)))*10000);
        }
    }

    // 상금을 못받는 나머지 순위에 대해서 0원으로 대입
    for(int i=32; i<=64; i++)
        b_rewards.push_back(0);

    // 입력 값을 저장할 pair을 원소로 갖는 vector
    vector<pair<int, int>> inputs;

    // 입력 횟수 T
    int T;
    scanf("%d", &T);

    // 입력
    while(T--){
        int a_input, b_input;
        scanf("%d %d", &a_input, &b_input);
        inputs.push_back(make_pair(a_input, b_input));
    }

    // 결과값 출력
    for(auto iter=inputs.begin(); iter!=inputs.end(); iter++){
        printf("%d\n", a_rewards[(*iter).first]+b_rewards[(*iter).second]);
    }

    return 0;
}