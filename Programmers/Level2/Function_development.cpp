#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;

    vector<int> days_left_until_deployment(progresses.size()); // 배포까지 남은 일 수를 각각 저장할 벡터

    for(int i = 0; i < progresses.size(); i++){
        // 배포까지 남은 일 수를 각각 올림하여 저장
        days_left_until_deployment[i] = int(ceil(double(100 - progresses[i])/double(speeds[i])));
    }

    // 현재 배포에 같이 배포되기 위한, 배포까지 남은 일 맨 처음값으로 초기화
    int current_max_day = days_left_until_deployment[0]; 
    int collected_progresses_count = 1; // 현재 배포에 포함되는 작업 갯수, 맨 처음부터니까 1로 초기화
    // 두 번째 작업부터 검사
    for(int progress_index = 1; progress_index < progresses.size(); progress_index++){
        
        if(days_left_until_deployment[progress_index] > current_max_day){
            // 만약 최대 일수보다 많이남은 작업이라면
            // 현재까지 수집한 작업들 갯수 저장
            answer.push_back(collected_progresses_count);

            // 갯수는 현재 작업부터 새로 수집이므로 1로 초기화
            collected_progresses_count = 1;
            // 남은 일 최대값 새로 설정
            current_max_day = days_left_until_deployment[progress_index];
        }else{
            // 최대 일수 이하의 작업이라면, 현재 배포에 포함
            collected_progresses_count++;
        }
    }

    // 현재까지 수집한 작업들 갯수 저장
    answer.push_back(collected_progresses_count);

    return answer;
}