#include <cstdio>
#include <vector>

using namespace std;

int main_10250(void){

    int t;

    scanf("%d", &t);

    vector<vector<int>> v(t, vector<int>(3));

    for(int i=0;i<t;i++){
        int h, w, n;
        scanf("%d %d %d", &h, &w, &n);
        v[i][0]=h;
        v[i][1]=w;
        v[i][2]=n;
    }

    int y=1, x=1;

    for(int i=0;i<t;i++){
        int h = v[i][0];
        int w = v[i][1];
        int n = v[i][2];
        int y, x;
        if(n%h==0){
            y = h;
            x = n/h;
        }else{
            y = n%h;
            x = n/h+1;
        }
        printf("%d", y);
        if(x/10==0){
            printf("0");
        }
        printf("%d\n", x);
    }

    return 0;
}