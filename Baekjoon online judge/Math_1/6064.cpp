#include <cstdio>
#include <vector>

using namespace std;

<<<<<<< HEAD
int main(void){

    int t;

    scanf("%d", &t);

    vector<vector<int>> test_case(t, vector<int>(4, 0));
    for(int i=0;i<t;i++){
        int m, n, x, y;
        scanf("%d %d %d %d", &m, &n, &x, &y);
        test_case[i][0] = m;
        test_case[i][1] = n;
        test_case[i][2] = x;
        test_case[i][3] = y;
    }

    for(int i=0;i<t;i++){
        double m, n, x, y;
        m = test_case[i][0];
        n = test_case[i][1];
        x = test_case[i][2];
        y = test_case[i][3];

        double r = (n*n*x-m*m*y)/(n*n-m*m);
        double check = r-int(r);
        if(m==n || check!=0.0){
            printf("%d\n", -1);
        }else{
            printf("%d\n", int(r));
        }
    }

=======
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

>>>>>>> f099413264bc9213c83f96307f321e3e95cfc4f1
    return 0;
}