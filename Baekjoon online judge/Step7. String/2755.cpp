#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

int main_2775(void){

    int t;

    scanf("%d", &t);

    vector<pair<int, int>> test_case;

    for(int i=0;i<t;i++){
        int k, n;
        scanf("%d", &k);
        scanf("%d", &n);

        test_case.push_back(make_pair(k, n));
    }

    for(int i=0;i<t;i++){
        int k, n;
        k = test_case[i].first;
        n = test_case[i].second;

        vector<vector<int>> apt(k+1, vector<int>(n+1, 0));
        for(int a=0;a<=k;a++){
            int downstairs_sum=0;
            for(int b=1;b<=n;b++){
                if(a==0){
                    apt[a][b]=b;
                }else{
                    downstairs_sum+=apt[a-1][b];
                    apt[a][b]=downstairs_sum;
                }
            }
        }

        printf("%d\n", apt[k][n]);
    }

    return 0;
}