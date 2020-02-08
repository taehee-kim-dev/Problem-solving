#include <cstdio>
#include <vector>

using namespace std;

int main(void){

    int N, M, K;

    scanf("%d %d %d", &N, &M, &K);

    vector<vector<int>> vec(N, vector<int>(0));
    vector<int> count_vec(N, 0);

    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            int input;

            scanf("%d", &input);

            vec[i].push_back(input);
        }
    }

    int result = -1;
    bool end = false;

    for(int j=0; j<M; j++){
        for(int i=0; i<N; i++){
            count_vec[i] += vec[i][j];
            if(count_vec[i]>=K){
                printf("%d %d", i+1, j+1);
                end=true;
                break;
            }
        }
        if(end==true)break;
    }
    

    return 0;
}