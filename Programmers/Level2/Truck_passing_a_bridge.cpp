#include <vector>
#include <deque>
#include <stack>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;

    // 시간 초 단위
    int total_time = 0;

    // 트럭 전체 수
    int total_trucks_count = truck_weights.size();

    // 대기하고있는 트럭들의 무게들을 저장할 스택
    stack<int> waiting_trucks_weights_stack;

    // 다리를 지난 트럭들의 무게들을 저장할 스택
    stack<int> finished_trucks_weights_stack;

    // 트럭의 무게를 맨 뒤 순서부터 스택에 저장
    for(int i = truck_weights.size() - 1; i >= 0; i--){
        waiting_trucks_weights_stack.push(truck_weights[i]);
    }

    // 다리를 덱으로 표현
    // 다리의 길이만큼 0으로 이루어진 덱을 만든다.
    // 0은 빈 공간.
    deque<int> bridge_deque(bridge_length, 0);
    
    // 현재 다리 위 트럭들의 총 무게
    int current_total_weight_on_bridge = 0;

    // 트럭들이 모두 다리를 건널 때 까지,
    while(finished_trucks_weights_stack.size() != total_trucks_count){

        // 다리의 맨 앞에 있는 요소를 빼낸다.
        int front_factor_weight = bridge_deque.front();
        bridge_deque.pop_front();

        // 만약 맨 앞에 있던 요소가 트럭이라면,
        if(front_factor_weight != 0){
            // 현재 다리 위 트럭들의 총 무게에서 현재 빠져나간 트럭의 무게를 뺀다.
            current_total_weight_on_bridge -= front_factor_weight;
            // 그리고 다리를 지난 트럭들을 저장할 스택에 저장한다.
            finished_trucks_weights_stack.push(front_factor_weight);
        }

        // 다음 트럭의 무게 기본값은 빈 공간으로 초기화
        int next_truck_weight = 0;

        // 만약 다음 트럭이 남아있다면,
        if(waiting_trucks_weights_stack.empty() != true){

            // 다리 위에 올라가야 할 다음 트럭의 무게를 스택에서 확인한다.
            next_truck_weight = waiting_trucks_weights_stack.top();
            
            // 다리 위에 다음 트럭이 올라갈 수 있는지 검사.
            if(current_total_weight_on_bridge + next_truck_weight <= weight){
                // 올라갈 수 있다면 다음 트럭을 대기 트럭 stack에서 뺌.
                waiting_trucks_weights_stack.pop();
            }else{
                // 올라갈 수 없다면 다음 트럭의 무게를 0으로 초기화하여 빈 공간으로 설정.
                next_truck_weight = 0;
            }
        }

        // 남아있지 않다면 자동으로 빈 공간 값이 됨.

        // 다음 요소를 다리 위로 올림(트럭의 무게 or 빈 공간)
        bridge_deque.push_back(next_truck_weight);
        // 현재 다리 위 트럭들의 총 무게에 방금 올라간 트럭의 무게를 추가한다.
        current_total_weight_on_bridge += next_truck_weight;

        // 시간을 1초 추가함.
        total_time++;
    }

    // 트럭들이 모두 다리를 건넜다면,
    answer = total_time;

    return answer;
}