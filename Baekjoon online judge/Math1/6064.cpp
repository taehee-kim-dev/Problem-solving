#include <cstdio>
#include <vector>

using namespace std;

int gcd(int a, int b){
    while(b!=0){
        int r=a%b;
        a=b;
        b=r;
    }
    return a;
}

int lcm(int a, int b){
    return a*b/gcd(a, b);
}

int main_6064(void){

    int T, M, N, x, y;

    scanf("%d", &T);

    vector<int> result;

    while(T--){
        scanf("%d %d %d %d", &M, &N, &x, &y);
        int max_year=lcm(M, N), result_year=-1;

        int i=0;
        while(x+i*M<=max_year){
            int check_y = (x+i*M)%N;

            if(check_y==y || (check_y==0 && N==y)){
                result_year=x+i*M;
                break;                      
            }
            i++;
        }
        result.push_back(result_year);
    }

    for(vector<int>::iterator iter=result.begin();iter<result.end();iter++)
        printf("%d\n", *iter);

    return 0;
}