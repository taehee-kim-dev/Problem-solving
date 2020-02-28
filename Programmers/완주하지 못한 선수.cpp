#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";

    // 두 벡터를 모두 정렬
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());

    // 두 벡터를 맨 앞 인덱스부터 하나씩 차례대로 검사
    for(int i = 0; i < participant.size(); i++){
        
        // 만약 두 벡터의 선수 이름이 서로 다르면,
        if(participant[i] != completion[i]){
            // participant[i]가 완주하지 못한 선수이다.
            return participant[i];
        }
    }

    // 만약 이 for문을 빠져나왔다면, 완주하지 못한 선수는 completion vector의 맨 마지막 원소

    return *(completion.end());
}