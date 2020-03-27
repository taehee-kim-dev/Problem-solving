#include <string>
#include <vector>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;

    for(int i = 0; i < skill_trees.size(); i++){

        // 현재 검사할 스킬 트리
        string current_skill_tree = skill_trees[i];

        // 스킬트리상에서 직전에 찾은 스킬의 위치 인덱스 값
        int before_found_skill_index = -2;

        // 현재 스킬트리의 가능 여부
        bool is_possible = true;

        for(int j = 0; j < skill.size(); j++){
            // 스킬트리상에서 스킬의 위치 인덱스를 찾는다
            int current_found_skill_index = current_skill_tree.find(skill[j]);
            // 찾았을 때,
            if(current_found_skill_index != string::npos){
                // 직전에 못찾았다면 무조건 불가능
                if(before_found_skill_index == string::npos){
                    is_possible = false;
                    break;
                }else if(current_found_skill_index < before_found_skill_index){
                    // 만약 직전에 찾은 인덱스 값보다 현재 찾은 인덱스 값이 작다면,
                    // 스킬 순서에 위배되므로 불가능한 스킬트리이다.
                    is_possible = false;
                    break;
                }
            }
            // 현재 찾은 인덱스 값을 직전 인덱스 값으로 업데이트
            before_found_skill_index = current_found_skill_index;
        }

        if(is_possible)
            answer++;
    }
    return answer;
}