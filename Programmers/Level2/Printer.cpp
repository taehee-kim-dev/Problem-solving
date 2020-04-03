#include <string>
#include <vector>
#include <utility>
#include <deque>

using namespace std;

/*
    중요도 : 숫자가 클 수록 중요하다.
    location : 내가 인쇄 요청한 문서의 인덱스(0부터 시작)
    return value : 번째의 수로, 1부터 시작
*/

int solution(vector<int> priorities, int location) {

    // 현재까지 인쇄된 문서의 수
    int current_print_count = 0;

    // queue<pair<중요도, 내 문서 여부>>
    deque<pair<int, bool>> documents_deque;

    // 중요도 별 문서의 개수
    vector<int> documents_count_per_priority_vec(10, 0);

    // 매개변수 벡터를 모두 덱에 push_back
    for(int document_index = 0; document_index < priorities.size(); document_index++){
        
        // 만약 내가 인쇄 요청한 문서의 인덱스라면, bool값을 true로
        if(document_index == location){
            documents_deque.push_back(make_pair(priorities[document_index], true));
        }else{
            documents_deque.push_back(make_pair(priorities[document_index], false));
        }

        // 현재 검사하고있는 문서의 중요도에 해당하는 문서의 개수 1 증가.
        documents_count_per_priority_vec[priorities[document_index]]++;

    }

    // 대기열에 있는 문서가 모두 인쇄될 때 까지 반복한다.
    while(documents_deque.size() > 0){

        // 맨 앞 문서를 임시 저장
        pair<int, bool> front_document = documents_deque.front();

        // 일단 맨 앞 문서를 대기열에서 빼낸다.
        documents_deque.pop_front();

        // 맨 앞 문서의 중요도
        int priority_of_front_document = front_document.first;

        // 프린트 가능 여부
        bool print_possible = true;

        // 맨 앞 문서의 중요도보다 큰 중요도를 갖는 문서의 개수가 1 이상인가?
        for(int priority = priority_of_front_document + 1; priority <= 9; priority++){
            // 맨 앞 문서의 중요도보다 큰 중요도를 갖는 문서의 개수가 하나라도 있다면,
            // 프린트 가능 여부를 false로 바꾸고, 바로 break.    
            if(documents_count_per_priority_vec[priority] > 0){
                print_possible = false;
                break;
            }
        }

        // 프린트 가능 여부에 따라
        if(print_possible){
            // 만약 프린트가 가능하다면,
            // 인쇄를 한다.
            // 그리고 현재까지 인쇄된 문서의 수 값을 1 증가시킨다.
            current_print_count++;
            // 그리고 중요도 별 문서의 개수를 저장한 벡터에서,
            // 현재 인쇄한 중요도의 문서의 개수를 1 감소시킨다.
            documents_count_per_priority_vec[priority_of_front_document]--;
            // 내가 인쇄를 요청한 문서라면
            // 현재까지 인쇄된 문서의 수 값을 반환한다. 
            if(front_document.second == true)
                return current_print_count;
        }else{
            // 프린트가 불가능하다면,
            // 맨 앞 문서를 대기열의 맨 뒤에 넣는다.
            documents_deque.push_back(front_document);
        }

    }
}

int main(void){

    solution(vector<int>{1, 1, 9, 1, 1, 1}, 0);

    return 0;
}