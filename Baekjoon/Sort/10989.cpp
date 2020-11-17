#include <cstdio>
#include <vector>

using namespace std;

int main(void){

    int N;
    scanf("%d", &N);

    vector<int> count(10001, 0);

    while(N--){
        int input_num;
        scanf("%d", &input_num);
        count[input_num]++;
    }

    for(int i=0; i<=10000; i++){
        for(int j=count[i]; j>0; j--){
            printf("%d\n", i);
        }
    }

    return 0;
}