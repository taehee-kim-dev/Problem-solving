#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
    최대한 많은 부서의 물품을 구매해 줄 수 있도록 (부서의 수가 최대여야 함.)
    각 부서당 신청금액에 부족하지 않게 정확히 지급.
    d : 부서별로 신청한 금액 / 길이 : 1이상 100 이하 / 각 원소 : 1이상 100,000이하
    budget : 총 예산 / 값 : 1이상 10,000,000이하
    최대 몇개의 부서에 물품 지원 가능?

    알고리즘 : 지원해 주는 부서의 수가 최대가 되어야 하므로, 
    부서별 신청 금액이 낮은 부서부터 지원해줘야 한다.
*/

int solution(vector<int> d, int budget) {
    int answer = 0;

    // 부서별 신청 금액을 오름차순으로 정렬.
    sort(d.begin(), d.end());

    // 0번 인덱스의 값부터 총 예산에서 빼면서, 뺄 때 마다 횟수를 계산. 해당 횟수가 답임.
    for(int i = 0; i < d.size(); i++){
        // 현재 체크중인 부서의 신청 금액이 남은 예산금액보다 클 경우,
        // 지원이 불가하므로 answer을 그대로 반환
        if(budget - d[i] < 0){
            return answer;
        }

        // 그렇지 않을 경우,
        // 해당 부서를 지원하고, answer의 값을 1 증가시킴.
        budget -= d[i];
        answer++;
    } 

    return answer;
}