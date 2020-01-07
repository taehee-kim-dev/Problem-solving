#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    // 원래 튜플을 담을 vector answer
    vector<int> answer;

    // string s 의 길이
    int s_len = s.length();
    // string에서 맨 앞, 맨 뒤 중괄후 제거해서 s2에 저장
    string s2 = s.substr(1, s_len-2);

    // string s에서 추출한 부분집합을 담을 2차원 벡터
    vector<vector<int>> subsets;

    // 부분집합의 번째 수를 저장할 변수
    int subset_count=0;

    // 하나의 부분집합을 담을 vector
    vector<int> tmp_subset;
    // 숫자를 임시 저장할 tmp_num;
    int tmp_num =0;

    // s2를 처음부터 끝까지 검사한다
    for(int i=0; i<s2.length(); i++){
            
        // 만약 현재 검사하고있는 문자가 숫자면
        if('0'<=s2.at(i) && s2.at(i)<='9'){
            // ','가 나올때까지 숫자 추출
            tmp_num*=10;
            tmp_num+=s2.at(i)-'0';
        
        // 만약 현재 검사하고 있는 문자가 "," 이면,
        }else if(s2.at(i)==','&&tmp_num!=0){
            // tmp_num을 tmp_subset에 추가하고 0으로 초기화
            tmp_subset.push_back(tmp_num);
            tmp_num=0;
        // 만약 현재 검사하고 있는 문자가 "}" 이면,
        }else if(s2.at(i)=='}'&&tmp_num!=0){
            // subsets vector에 tmp_subset을 추가한다
            tmp_subset.push_back(tmp_num);
            tmp_num=0;
            subsets.push_back(tmp_subset);
            tmp_subset.clear();
        }
    }

    // 가장 긴 부분집합 찾기
    // 가장 긴 부분집합의 사이즈 저장할 변수
    int max_subset_size=0;

    for(int i=0; i<subsets.size(); i++){
        if(subsets.size()>max_subset_size)
            max_subset_size = subsets.size();
    }

    // 모든 원소들을 저장할 벡터
    vector<int> all_elements;

    // 가장 긴 부분집합을 찾아서
    for(int i=0; i<subsets.size(); i++){
        if(subsets[i].size()==max_subset_size){
            // 가장 긴 부분집합의 모든 원소를 all_elements에 pushback
            for(int j=0; j<max_subset_size; j++){
                all_elements.push_back(subsets[i][j]);
            }
        }
    }

    // 각 원소의 존재 빈도수를 저장할 벡터
    vector<int> frequency_of_all_elements(max_subset_size, 0);

    for(int m=0; m<all_elements.size(); m++){
        int element_count=0;
        for(int i=0; i<subsets.size(); i++){
            for(int j=0; j<subsets[i].size(); j++){
                if(subsets[i][j]==all_elements[m])
                    element_count++;
            }
        }
        frequency_of_all_elements[m] = element_count;
    }



    // 최대 빈도수를 갖는 원소를 answer에 pushback 시키고, 
    // 해당 원소를 all_element에서 삭제

    // frequency_of_all_elements에서 최댓값의 인덱스는?

    for(int i=0; i<all_elements.size(); i++){
        vector<int>::iterator iter;
        iter = max_element(frequency_of_all_elements.begin(), frequency_of_all_elements.end());
        int index_of_max_element = distance(frequency_of_all_elements.begin(), iter);

        answer.push_back(all_elements[index_of_max_element]);
        frequency_of_all_elements[index_of_max_element] = 0;
    }

    return answer;
}

int main(void){

    string s = "{{4,2,3},{3},{2,3,4,1},{2,3}}";

    vector<int> result = solution(s);

    for(vector<int>::iterator iter=result.begin(); iter!=result.end(); iter++){
        printf("%d ", *iter);
    }

    return 0;
}