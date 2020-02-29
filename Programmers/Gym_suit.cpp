#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;

    // 전체 학생 크기 + 1 만큼 lost, reserve에 관한 bool 벡터를 모두 false로 초기화하여 만든다.
    vector<bool> lost_vec(n + 1, false);
    vector<bool> reserve_vec(n + 1, false);

    // lost vector, reserve vector 각각에 존재하는 학생번호를
    // bool vector의 인덱스로 하여 true값으로 바꿈.

    for(int i = 0; i < lost.size(); i++){
        lost_vec[lost[i]] = true;
    }

    for(int i = 0; i < reserve.size(); i++){
        reserve_vec[reserve[i]] = true;
    }

    // 여벌 체육복을 가져온 학생중에서 체육복을 도난당한 학생은,
    // 결국 도난당하지도 않고, 여벌 체육복을 가져오지도 않은 학생과 입장이 같다.
    // 따라서, lost_vec과 reserve_vec에서 같은 인덱스에서 모두 true값이면,
    // false로 둘다 바꿔준다.

    for(int i = 1; i <= n; i++){
        if(lost_vec[i] == true && reserve_vec[i] == true){
            lost_vec[i] = false;
            reserve_vec[i] = false;
        }
    }

    // 이제 여벌 체육복을 가져온 학생과 체육복을 도난당한 학생중에 겹치는 학생은 없다.


    /*
        체육복을 도난당한 학생들을 검사한다.
        
        case 1) 체육복을 도난당한 학생의 번호 - 1 학생이 여벌 체육복을 가져왔는지 먼저 확인하고,
        가져왔다면 빌린다.
        즉, reserve_vec, lost_vec에서 빌린 학생의 번호와 빌려준 학생의 번호를  각각 인덱스로하여 
        false값으로 바꾼다.
        빌렸다면 체육복을 도난당한 다음 학생을 검사한다.
        
        case 2) 만약 체육복을 도난당한 학생의 번호 - 1 학생이 여벌 체육복을 가져오지 않았다면,
        체육복을 도난당한 학생의 번호 + 1 학생이 여벌 체육복을 가져왔는지 확인한다.
        가져왔다면 빌린다.
        빌렸다면 체육복을 도난당한 다음 학생을 검사한다.
        
        case 3) 위 두 케이스에 해당하지 않으면, 체육복을 도난당한 다음 학생을 검사한다.
    */
    
    for(int i = 1; i <= n; i++){

        if(lost_vec[i] == true){

            if(reserve_vec[i - 1] == true){
                reserve_vec[i - 1] = false;
                lost_vec[i] = false;
                continue;
            }

            if(reserve_vec[i + 1] == true){
                reserve_vec[i + 1] = false;
                lost_vec[i] = false;
                continue;
            }

        }
    }
    
    // 체육수업을 들을 수 있는 학생의 최댓값 = 전체 학생 수 n으로 놓는다.
    answer = n;

    // lost_vec을 처음부터 끝까지 검사하면서,
    // 체육복을 도난당했으나 빌리지 못한 학생을 만날 때 마다 answer의 값을 1씩 감소시킨다.
    for(int i = 1; i <= n; i++){
        if(lost_vec[i] == true)
            answer--;
    }

    return answer;
}