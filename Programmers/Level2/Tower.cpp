#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> heights) {
    vector<int> answer;

    // 맨 왼쪽 탑부터 순서대로,
    // 자신의  왼쪽에 있는 탑부터 처음 탑까지 순서대로 검사한다.
    // 맨 처음으로 나오는, 자기 자신보다 높은 높이를 가진 탑에,
    // 현재 검사하고 있는 탑의 신호가 수신된다.
    for(int tower_index = 0; tower_index < heights.size(); tower_index++){

        // 현재 검사하는 타워의 바로 왼쪽 타워부터 인덱스 -1 까지 순서대로 검사
        for(int reception_tower_check_index = tower_index - 1; reception_tower_check_index >= -1; reception_tower_check_index--){
            
            // 만약 -1 이라면 어느 타워에서도 수신하지 못하는 것이므로,
            if(reception_tower_check_index == -1){
                // 정답 벡터에 0 추가
                answer.push_back(0);
                // 바로 다음 탑을 검사한다.
                break;
            }

            // 만약 현재 검사하고 있는 타워보다 높은 높이를 갖고 있다면,
            if(heights[reception_tower_check_index] > heights[tower_index]){
                // 정답 벡터에 현재 체크 인덱스에 +1을 하여 추가.
                // 왜냐하면 정답은 "번째"로 기록되어야 하기 때문.
                answer.push_back(reception_tower_check_index + 1);
                // 바로 다음 탑 검사
                break;
            }
        }
    } 
    
    return answer;
}