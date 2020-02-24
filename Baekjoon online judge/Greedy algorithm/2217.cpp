#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int N;
// 각 로프가 버틸 수 있는 중량값들
vector<int> ropes;
// 각 경우마다 로프가 버틸 수 있는 최대 중량값들
vector<int> weights;

// 내림차순 정렬을 위한 비교함수
bool compare(int a, int b){
    return a > b;
}


void solve(){
    // 로프들을 버틸 수 있는 중량값을 기준으로 내림차순 정렬
    sort(ropes.begin(), ropes.end(), compare);

    // 0번째 로프부터 i번째 로프까지 선택했을 때,
    // 전체 로프가 총 버틸수 있는 무게는,
    // i번째 로프(제일 버틸 수 있는 무게가 낮은 로프)가 버틸 수 있는 무게 * 선택된 총 로프의 갯수 이다.
    // 이렇게 얻어진 여러가지 경우의 로프들이 버틸 수 있는 총 무게들을 weights 벡터에 push_back 해준다. 
    for(int i=0; i<ropes.size(); i++){
        weights.push_back(ropes[i] * (i + 1));
    }

    // weights 벡터를 내림차순으로 정렬하면, 맨 처음 원소값이 최대값이다.
    sort(weights.begin(), weights.end(), compare);

    printf("%d", weights[0]);
}

void input(){
    scanf("%d", &N);
    int T = N;
    while(T--){
        int input;
        scanf("%d", &input);
        ropes.push_back(input);
    }
}

int main(void){

    input();
    solve();
    
    return 0;
}