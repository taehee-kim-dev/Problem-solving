#include <cstdio>

using namespace std;

int N, M;
int result[8]; // 선택한 수들을 저장할 배열

void solve(int level, int min){ // 매개변수는 트리의 레벨

    // 만약 트리의 현재 레벨이, 선택해야 하는 갯수와 같다면
    if(level == M){
        // 선택한 수들을 선택해야 하는 갯수 만큼 모두 출력
        for(int i=0; i<M; i++)
            printf("%d ", result[i]);

        printf("\n"); // 개행
        return;
    }

    // 고려하는 수 들은
    // 직전 레벨에서 매개변수로 전달한 min값(최소값)부터 N까지임
    for(int i=min; i<=N; i++){
        // 현재 선택한 수는 i
        // i를 result배열의 level 인덱스에 저장
        result[level] = i;
        
        // 함수 재귀호출
        // level + 1의 값을 다음 레벨값으로 준다.
        // i + 1의 값을 다음 숫자 고려시의 최소값으로 준다.
        solve(level + 1, i + 1);
    }
}

int main(void){

    scanf("%d %d", &N, &M); // 입력

    solve(0, 1); // 트리의 맨 처음 레벨은 0, 최소값은 1

    return 0;
}