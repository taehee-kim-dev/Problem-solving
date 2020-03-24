#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

/*
    N : 전체 스테이지의 개수
    실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    반환값 : 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열
*/

bool compare(const pair<int, double> &p1, const pair<int, double> &p2){
    if(p1.second == p2.second){
        return p1.first < p2.first;
    }else{
        return p1.second > p2.second;
    }
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;

    // 전체 현황
    // [스테이지 인덱스 : 스테이지 번호 -1][스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수, 스테이지에 도달한 플레이어 수]
    vector<vector<int>> total_stats(N + 1, vector<int>(2, 0));

    for(int user_index = 0; user_index < stages.size(); user_index++){
        
        // stages[user_index]의 값은 현재 사용자가 멈춰있는 스테이지의 번호
        int current_stage = stages[user_index];

        // current_stage 이하의 스테이지에 도달한 플레이어 값 모두 1씩 증가
        for(int stage_index = 0; stage_index < current_stage; stage_index++){
            total_stats[stage_index][1]++;
        }

        // current_stage 스테이지는 도달했으나 아직 클리어하지 못했으므로
        // current_stage의 클리어하지 못한 플레이어의 수 1 증가
        (total_stats[current_stage - 1][0])++;
    }

    // 실패율 저장 벡터 [stage의 index, 실패율]
    vector<pair<int, double>> failure_rate;

    for(int stage_index = 0; stage_index < N; stage_index++){
        if(total_stats[stage_index][1] == 0){
            failure_rate.push_back(make_pair(stage_index + 1, 0.0));
            
        }else{
            failure_rate.push_back(make_pair(stage_index + 1, 
                double(total_stats[stage_index][0]) / double(total_stats[stage_index][1])));
        }
    }



    sort(failure_rate.begin(), failure_rate.end(), compare);

    for(int i = 0; i < N; i++){
        answer.push_back(failure_rate[i].first);
    }

    return answer;
}

int main(void){

    vector<int> input{4,4,4,4,4};
    
    solution(4, input);

    return 0;
}