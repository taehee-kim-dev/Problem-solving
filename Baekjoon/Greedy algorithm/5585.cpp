#include <cstdio>

using namespace std;

int N;
int changes[6] = {500, 100, 50, 10, 5, 1};
int result = 0;

void solve(){
    int totalChange = 1000 - N;
    // 큰 가치의 동전부터 고려
    for(int i=0; i<6; i++){
        // 한 동전의 가치가 채워야하는 잔돈의 총 가치보다는 같거나 작아야 한다.
        if(changes[i] <= totalChange){
            // 나누기 결과의 몫이 해당 동전의 최대 개수이므로 결과값에 더해준다.
            result += (totalChange / changes[i]);
            // 나누기 결과의 나머지가 채워야하는 남은 잔돈이다.
            totalChange %= changes[i];
        }
    }

    printf("%d", result);
}

void input(){
    scanf("%d", &N);
}

int main(void){

    input();
    solve();

    return 0;
}