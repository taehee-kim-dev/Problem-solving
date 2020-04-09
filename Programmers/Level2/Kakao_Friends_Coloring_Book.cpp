#include <vector>
#include <algorithm>

using namespace std;

/*
    영역 : 영역이란 상하좌우로 연결된 같은 색상의 공간
    난이도 : 영역의 수
    return : 그림에 몇 개의 영역이 있는지와 가장 큰 영역은 몇 칸으로 이루어져 있는지를
    원소가 두 개인 정수 배열로
*/

int M, N;
vector<vector<int>> PICTURE_VEC;

// 현재 영역의 넓이
int CURRENT_SIZE_OF_AREA;

// 영역 별 넓이를 찾는 함수
void find_size_of_area(int x, int y, int color){

    // 만약 검사하는 영역이 존재하지 않거나,
    // 색칠하지 않은 영역이거나 (값이 0)
    // 이미 체크한 영역이라면 (값이 -1)
    // 현재 검사하고있는 색과 다른 색이라면
    // return
    if(x < 0 || y < 0 || M <= x || N <= y || PICTURE_VEC[x][y] == 0 || PICTURE_VEC[x][y] == -1
        || PICTURE_VEC[x][y] != color)
        return;

    // 위의 경우에 해당하지 않는다면,
    // 같은 영역이므로
    // 현재 영역의 넓이 값 1 증가
    CURRENT_SIZE_OF_AREA++;
    // 현재 영역의 값 -1로 체크
    PICTURE_VEC[x][y] = -1;
    
    // 다음 영역 검사
    find_size_of_area(x, y - 1, color); // 상
    find_size_of_area(x, y + 1, color); // 하
    find_size_of_area(x - 1, y, color); // 좌
    find_size_of_area(x + 1, y, color); // 우
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    vector<int> answer(2);

    M = m;
    N = n;
    PICTURE_VEC = picture;

    // 영역 별 넓이
    vector<int> size_of_each_area_vec;

    // PICTURE를 검사하면서
    for(int row = 0; row < PICTURE_VEC.size(); row++){
        for(int col = 0; col < (PICTURE_VEC[row]).size(); col++){
            // 색상값이 나오면
            if(PICTURE_VEC[row][col] != -1 && PICTURE_VEC[row][col] != 0){
                // 현재 원소부터 영역의 넓이를 체크해야 하므로,
                // 현재 영역의 넓이를 0으로 초기화
                CURRENT_SIZE_OF_AREA = 0;
                // 현재 좌표, 색상값으로 함수를 호출하여 영역의 넓이 구함.
                find_size_of_area(row, col, PICTURE_VEC[row][col]);
                // 모두 구했으면, 현재 영역값을 결과값 벡터에 추가.
                size_of_each_area_vec.push_back(CURRENT_SIZE_OF_AREA);
            }
        }
    }

    // 모든 측정을 끝냈다면,
    number_of_area = size_of_each_area_vec.size();
    max_size_of_one_area = *(max_element(size_of_each_area_vec.begin(), size_of_each_area_vec.end()));


    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}