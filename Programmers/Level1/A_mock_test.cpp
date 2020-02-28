#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
    1번 수포자 : (1, 2, 3, 4, 5) 반복
    2번 수포자 : (2, 1, 2, 3, 2, 4, 2, 5) 반복
    3번 수포자 : (3, 3, 1, 1, 2, 2, 4, 4, 5, 5) 반복
*/

vector<int> solution(vector<int> answers) {
    vector<int> answer;

    // 인덱스 0 : 1번 수포자
    // 인덱스 1 : 2번 수포자
    // 인덱스 2 : 3번 수포자

    // 순서대로 각 수포자의 찍는 패턴
    vector<vector<int>> patterns{
        {1, 2, 3, 4, 5},
        {2, 1, 2, 3, 2, 4, 2, 5},
        {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
    };

    // 순서대로 각 수포자의 인덱스
    vector<int> indexes{0, 0, 0};

    // 순서대로 각 수포자의 점수
    vector<int> scores{0, 0, 0}; 
    
    
    // 시험 문제의 답을 처음부터 순서대로 검사
    for(int i = 0; i < answers.size(); i++){
        
        // 해당 문제의 답을 맞춘 수포자의 score 1씩 증가
        // 수포자 한명씩 해당 문제의 답이 맞는지 검사
        // 검사하면서 연산 직후 각 수포자의 인덱스를 1씩 증가
        for(int j = 0; j < 3; j++){
            if(answers[i] == patterns[j][indexes[j]++])
                scores[j]++;

            // 만약 수포자의 인덱스 범위가 넘어가면, 0으로 초기화
            if(indexes[j] >= patterns[j].size())
                indexes[j] = 0;
        }
    }

    // 모든 문제의 답을 확인했으면, 수포자의 점수들 중 최대값을 찾음.
    int max_score = *max_element(scores.begin(), scores.end());

    // 최대값을 가진 수포자의 인덱스 + 1을 answer 벡터에 추가함.
    for(int i = 0; i < 3; i++){
        if(max_score == scores[i])
            answer.push_back(i+1);
    }

    return answer;
}