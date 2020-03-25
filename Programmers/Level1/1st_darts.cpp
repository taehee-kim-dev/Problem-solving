#include <string>
#include <cctype>
#include <cmath>
#include <vector>

using namespace std;

int solution(string dartResult) {
    int answer = 0;

    int stage = 1;
    vector<int> scores(4, 0);

    for(int i = 0; i < dartResult.length(); i++){
        
        // 점수 기준으로 끊어서 검사
        if(isdigit(dartResult[i])){
            // 현재 검사하고 있는 값이 숫자값(점수) 라면,

            // 10의 1이라면
            if(dartResult[i] == '1' && dartResult[i + 1] == '0')
                continue;

            // 10의 0이라면
            if(dartResult[i - 1] == '1' && dartResult[i] == '0'){
                scores[stage] = 10;
            }else
                scores[stage] = dartResult[i] - '0'; // 현재 점수값 저장.
            
            // 보너스 적용
            switch (dartResult[i + 1]){
                case 'D':
                    scores[stage] = int(pow(double(scores[stage]), 2.0));
                    break;
                case 'T':
                    scores[stage] = int(pow(double(scores[stage]), 3.0));
                    break;
            }

            if(i + 2 <= dartResult.size() - 1){
                // [옵션]이 존재할 시 적용
                switch (dartResult[i + 2]){
                    case '*':

                        // 현재 점수를 2배로
                        scores[stage] *= 2;

                        // 직전 점수가 존재할 시, 직전 점수도 2배로
                        if(stage >= 1)
                            scores[stage - 1] *= 2;

                        break;
                    case '#':

                        // 현재 점수에 -1.0 곱하기
                        scores[stage] *= (-1);

                        break;
                }
            }
            stage++;
            
        }
    }

    for(int i = 1; i <= 3; i++){
        answer += scores[i];
    }

    return answer;
}