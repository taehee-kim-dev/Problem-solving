#include <cstdio>
#include <vector>

using namespace std;

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

    return 0;
}