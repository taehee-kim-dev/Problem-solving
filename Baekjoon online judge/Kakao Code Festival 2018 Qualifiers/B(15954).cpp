#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

double get_m(int i, int j, vector<int> &vec){

    double m=0.0;

    for(int l=i; l<=j; l++)
        m+=vec[l];

    m/=(j-i+1);

    return m;
}

double get_v(int i, int j, vector<int> &vec){

    double v=0.0;
    double m = get_m(i, j, vec);

    for(int l=i; l<=j; l++){
        v+=pow(vec[l]-m, 2.0);
    }

    v/=(j-i+1);
    
    return v;
}

int main(void){

    vector<int> dolls;
    vector<double> results;

    int N, K;

    scanf("%d %d", &N, &K);

    int T=N;

    while(T--){
        int input;
        scanf("%d", &input);
        dolls.push_back(input);
    }

    for(int k=K; k<=N; k++){
        for(int i=0; i<N-k+1; i++){
            
                double result = sqrt(get_v(i, i+k-1, dolls));
                results.push_back(result);
            }
    }

    sort(results.begin(), results.end());

    printf("%f", results[0]);

    return 0;
}